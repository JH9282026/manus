# Applications and Case Studies

Real-world RL applications, game playing, robotics, autonomous systems, and implementation examples.

---

## Game Playing

### Atari Games with DQN

```python
import gym
from stable_baselines3 import DQN
from stable_baselines3.common.atari_wrappers import AtariWrapper
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv

# Create Atari environment
env = gym.make('ALE/Breakout-v5')
env = AtariWrapper(env)
env = DummyVecEnv([lambda: env])
env = VecFrameStack(env, n_stack=4)

# Train DQN
model = DQN(
    'CnnPolicy',
    env,
    learning_rate=1e-4,
    buffer_size=100000,
    learning_starts=100000,
    batch_size=32,
    tau=1.0,
    gamma=0.99,
    train_freq=4,
    gradient_steps=1,
    target_update_interval=10000,
    exploration_fraction=0.1,
    exploration_final_eps=0.01,
    verbose=1,
    tensorboard_log='./logs/'
)

model.learn(total_timesteps=10000000)
model.save('dqn_breakout')
```

### AlphaZero-Style Game AI

```python
import torch
import torch.nn as nn
import numpy as np
from collections import defaultdict
import math

class GameState:
    """Abstract game state interface"""
    def get_legal_actions(self):
        raise NotImplementedError
    
    def take_action(self, action):
        raise NotImplementedError
    
    def is_terminal(self):
        raise NotImplementedError
    
    def get_reward(self):
        raise NotImplementedError
    
    def to_tensor(self):
        raise NotImplementedError

class AlphaZeroNetwork(nn.Module):
    def __init__(self, input_shape, num_actions):
        super(AlphaZeroNetwork, self).__init__()
        
        # Shared representation
        self.conv = nn.Sequential(
            nn.Conv2d(input_shape[0], 128, 3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Conv2d(128, 128, 3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU()
        )
        
        # Policy head
        self.policy_head = nn.Sequential(
            nn.Conv2d(128, 2, 1),
            nn.BatchNorm2d(2),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(2 * input_shape[1] * input_shape[2], num_actions)
        )
        
        # Value head
        self.value_head = nn.Sequential(
            nn.Conv2d(128, 1, 1),
            nn.BatchNorm2d(1),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(input_shape[1] * input_shape[2], 256),
            nn.ReLU(),
            nn.Linear(256, 1),
            nn.Tanh()
        )
    
    def forward(self, x):
        features = self.conv(x)
        policy = self.policy_head(features)
        value = self.value_head(features)
        return policy, value

class MCTSNode:
    def __init__(self, state, parent=None, action=None, prior=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.prior = prior
        
        self.children = {}
        self.visit_count = 0
        self.value_sum = 0
    
    def value(self):
        if self.visit_count == 0:
            return 0
        return self.value_sum / self.visit_count
    
    def ucb_score(self, c_puct=1.0):
        u = c_puct * self.prior * math.sqrt(self.parent.visit_count) / (1 + self.visit_count)
        return self.value() + u
    
    def select_child(self):
        return max(self.children.values(), key=lambda node: node.ucb_score())
    
    def expand(self, policy_probs):
        for action, prob in enumerate(policy_probs):
            if action in self.state.get_legal_actions():
                next_state = self.state.take_action(action)
                self.children[action] = MCTSNode(next_state, parent=self, action=action, prior=prob)
    
    def backup(self, value):
        self.visit_count += 1
        self.value_sum += value
        if self.parent:
            self.parent.backup(-value)  # Negate for opponent

class AlphaZeroAgent:
    def __init__(self, network, num_simulations=800):
        self.network = network
        self.num_simulations = num_simulations
    
    def search(self, root_state):
        root = MCTSNode(root_state)
        
        # Expand root
        with torch.no_grad():
            policy_logits, value = self.network(root_state.to_tensor())
            policy_probs = torch.softmax(policy_logits, dim=-1).numpy()
        root.expand(policy_probs)
        
        # Run simulations
        for _ in range(self.num_simulations):
            node = root
            
            # Selection
            while node.children and not node.state.is_terminal():
                node = node.select_child()
            
            # Expansion and evaluation
            if not node.state.is_terminal():
                with torch.no_grad():
                    policy_logits, value = self.network(node.state.to_tensor())
                    policy_probs = torch.softmax(policy_logits, dim=-1).numpy()
                node.expand(policy_probs)
                value = value.item()
            else:
                value = node.state.get_reward()
            
            # Backup
            node.backup(value)
        
        # Return visit count distribution as policy
        visit_counts = np.array([root.children[a].visit_count if a in root.children else 0
                                 for a in range(len(policy_probs))])
        return visit_counts / visit_counts.sum()
```

---

## Robotics Control

### Robot Arm Reaching Task

```python
import gym
import pybullet_envs
from stable_baselines3 import SAC

# Create robot environment
env = gym.make('ReacherBulletEnv-v0')

# Train SAC (good for continuous control)
model = SAC(
    'MlpPolicy',
    env,
    learning_rate=3e-4,
    buffer_size=1000000,
    learning_starts=10000,
    batch_size=256,
    tau=0.005,
    gamma=0.99,
    train_freq=1,
    gradient_steps=1,
    ent_coef='auto',
    verbose=1
)

model.learn(total_timesteps=1000000)
model.save('sac_reacher')

# Evaluate
obs = env.reset()
for _ in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        obs = env.reset()
```

### Sim-to-Real Transfer

```python
class DomainRandomization:
    """Randomize simulation parameters for robust policies"""
    def __init__(self, env):
        self.env = env
    
    def randomize_physics(self):
        # Randomize mass
        mass = np.random.uniform(0.8, 1.2) * self.env.default_mass
        self.env.set_mass(mass)
        
        # Randomize friction
        friction = np.random.uniform(0.5, 1.5) * self.env.default_friction
        self.env.set_friction(friction)
        
        # Randomize actuator strength
        strength = np.random.uniform(0.9, 1.1)
        self.env.set_actuator_strength(strength)
    
    def randomize_observations(self, obs):
        # Add sensor noise
        noise = np.random.normal(0, 0.01, size=obs.shape)
        return obs + noise
    
    def reset(self):
        self.randomize_physics()
        obs = self.env.reset()
        return self.randomize_observations(obs)
    
    def step(self, action):
        obs, reward, done, info = self.env.step(action)
        obs = self.randomize_observations(obs)
        return obs, reward, done, info

# Use domain randomization
env = DomainRandomization(gym.make('ReacherBulletEnv-v0'))
model = SAC('MlpPolicy', env)
model.learn(total_timesteps=1000000)
```

### Imitation Learning (Behavioral Cloning)

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

class ExpertDataset(Dataset):
    def __init__(self, states, actions):
        self.states = torch.FloatTensor(states)
        self.actions = torch.FloatTensor(actions)
    
    def __len__(self):
        return len(self.states)
    
    def __getitem__(self, idx):
        return self.states[idx], self.actions[idx]

class BehavioralCloningAgent:
    def __init__(self, state_dim, action_dim, hidden_dim=256):
        self.policy = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, action_dim),
            nn.Tanh()
        )
        self.optimizer = optim.Adam(self.policy.parameters(), lr=1e-3)
    
    def train(self, expert_states, expert_actions, epochs=100, batch_size=64):
        dataset = ExpertDataset(expert_states, expert_actions)
        dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
        
        for epoch in range(epochs):
            total_loss = 0
            for states, actions in dataloader:
                predicted_actions = self.policy(states)
                loss = nn.MSELoss()(predicted_actions, actions)
                
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
                
                total_loss += loss.item()
            
            if epoch % 10 == 0:
                print(f"Epoch {epoch}: Loss = {total_loss / len(dataloader):.4f}")
    
    def choose_action(self, state):
        with torch.no_grad():
            state_tensor = torch.FloatTensor(state)
            action = self.policy(state_tensor).numpy()
        return action

# Collect expert demonstrations
expert_states = []
expert_actions = []

# ... collect data from expert policy or human demonstrations ...

# Train behavioral cloning agent
agent = BehavioralCloningAgent(state_dim=env.observation_space.shape[0],
                                action_dim=env.action_space.shape[0])
agent.train(expert_states, expert_actions)
```

---

## Autonomous Systems

### Autonomous Driving (Lane Keeping)

```python
import gym
import highway_env

# Install: pip install highway-env

env = gym.make('highway-v0')
env.configure({
    "observation": {
        "type": "Kinematics",
        "vehicles_count": 5,
        "features": ["presence", "x", "y", "vx", "vy", "cos_h", "sin_h"],
        "absolute": False
    },
    "action": {
        "type": "ContinuousAction"
    },
    "duration": 40,
    "policy_frequency": 2
})

# Train TD3 for continuous control
from stable_baselines3 import TD3

model = TD3(
    'MlpPolicy',
    env,
    learning_rate=1e-3,
    buffer_size=200000,
    learning_starts=10000,
    batch_size=100,
    tau=0.005,
    gamma=0.99,
    policy_delay=2,
    target_policy_noise=0.2,
    target_noise_clip=0.5,
    verbose=1
)

model.learn(total_timesteps=500000)
model.save('td3_highway')
```

### Drone Navigation

```python
import gym
import gym_pybullet_drones
from gym_pybullet_drones.envs.single_agent_rl import HoverAviary

# Create drone environment
env = HoverAviary()

# Train PPO
from stable_baselines3 import PPO

model = PPO(
    'MlpPolicy',
    env,
    learning_rate=3e-4,
    n_steps=2048,
    batch_size=64,
    n_epochs=10,
    gamma=0.99,
    verbose=1
)

model.learn(total_timesteps=1000000)

# Test trained policy
obs = env.reset()
for _ in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    if done:
        obs = env.reset()
```

---

## Resource Management

### Energy Grid Optimization

```python
class EnergyGridEnv(gym.Env):
    def __init__(self, n_generators=5, n_timesteps=24):
        super(EnergyGridEnv, self).__init__()
        
        self.n_generators = n_generators
        self.n_timesteps = n_timesteps
        
        # Action: power output for each generator (continuous)
        self.action_space = spaces.Box(
            low=0, high=1, shape=(n_generators,), dtype=np.float32
        )
        
        # Observation: demand, time, generator states
        self.observation_space = spaces.Box(
            low=-np.inf, high=np.inf, shape=(n_generators + 2,), dtype=np.float32
        )
        
        self.current_timestep = 0
        self.demand_profile = self._generate_demand_profile()
    
    def _generate_demand_profile(self):
        # Simulate daily demand pattern
        t = np.linspace(0, 24, self.n_timesteps)
        base_demand = 50
        peak_demand = 100
        demand = base_demand + (peak_demand - base_demand) * (
            0.5 * (1 + np.sin(2 * np.pi * (t - 6) / 24))
        )
        return demand
    
    def reset(self):
        self.current_timestep = 0
        self.generator_states = np.ones(self.n_generators)
        return self._get_observation()
    
    def _get_observation(self):
        demand = self.demand_profile[self.current_timestep]
        time_of_day = self.current_timestep / self.n_timesteps
        return np.concatenate([[demand, time_of_day], self.generator_states])
    
    def step(self, action):
        # Scale action to actual power output
        max_power = np.array([100, 80, 60, 50, 40])  # Generator capacities
        power_output = action * max_power
        total_output = power_output.sum()
        
        # Current demand
        demand = self.demand_profile[self.current_timestep]
        
        # Compute reward
        # Penalize: generation cost, demand mismatch, emissions
        generation_cost = np.sum(power_output * np.array([0.05, 0.04, 0.06, 0.03, 0.07]))
        demand_mismatch = abs(total_output - demand)
        emissions = np.sum(power_output * np.array([0.8, 0.6, 0.9, 0.3, 0.2]))
        
        reward = -(generation_cost + 10 * demand_mismatch + 5 * emissions)
        
        # Update state
        self.current_timestep += 1
        done = self.current_timestep >= self.n_timesteps
        
        return self._get_observation(), reward, done, {}

# Train agent
env = EnergyGridEnv()
model = SAC('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=100000)
```

---

## Finance and Trading

### Stock Trading Agent

```python
import gym
from gym import spaces
import pandas as pd
import numpy as np

class TradingEnv(gym.Env):
    def __init__(self, df, initial_balance=10000, commission=0.001):
        super(TradingEnv, self).__init__()
        
        self.df = df
        self.initial_balance = initial_balance
        self.commission = commission
        
        # Action: [hold, buy, sell]
        self.action_space = spaces.Discrete(3)
        
        # Observation: [balance, shares, price, technical indicators]
        self.observation_space = spaces.Box(
            low=-np.inf, high=np.inf, shape=(10,), dtype=np.float32
        )
        
        self.reset()
    
    def reset(self):
        self.balance = self.initial_balance
        self.shares = 0
        self.current_step = 0
        self.total_profit = 0
        return self._get_observation()
    
    def _get_observation(self):
        row = self.df.iloc[self.current_step]
        return np.array([
            self.balance / self.initial_balance,
            self.shares,
            row['close'],
            row['volume'],
            row['sma_20'],
            row['sma_50'],
            row['rsi'],
            row['macd'],
            row['bb_upper'],
            row['bb_lower']
        ], dtype=np.float32)
    
    def step(self, action):
        current_price = self.df.iloc[self.current_step]['close']
        
        # Execute action
        if action == 1:  # Buy
            shares_to_buy = self.balance // (current_price * (1 + self.commission))
            if shares_to_buy > 0:
                cost = shares_to_buy * current_price * (1 + self.commission)
                self.balance -= cost
                self.shares += shares_to_buy
        
        elif action == 2:  # Sell
            if self.shares > 0:
                revenue = self.shares * current_price * (1 - self.commission)
                self.balance += revenue
                self.shares = 0
        
        # Move to next step
        self.current_step += 1
        done = self.current_step >= len(self.df) - 1
        
        # Calculate reward (portfolio value change)
        portfolio_value = self.balance + self.shares * current_price
        reward = (portfolio_value - self.initial_balance) / self.initial_balance
        
        return self._get_observation(), reward, done, {}

# Load stock data
df = pd.read_csv('stock_data.csv')
# ... compute technical indicators ...

# Train agent
env = TradingEnv(df)
model = PPO('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=100000)
```

---

## Recommendation Systems

### Contextual Bandits for Recommendations

```python
class ContextualBandit:
    def __init__(self, n_actions, context_dim, alpha=1.0):
        self.n_actions = n_actions
        self.context_dim = context_dim
        self.alpha = alpha
        
        # Linear UCB parameters
        self.A = [np.identity(context_dim) for _ in range(n_actions)]
        self.b = [np.zeros(context_dim) for _ in range(n_actions)]
    
    def choose_action(self, context):
        # Compute UCB for each action
        ucb_values = []
        for a in range(self.n_actions):
            A_inv = np.linalg.inv(self.A[a])
            theta = A_inv @ self.b[a]
            
            # UCB = expected reward + exploration bonus
            expected_reward = context @ theta
            exploration_bonus = self.alpha * np.sqrt(context @ A_inv @ context)
            ucb = expected_reward + exploration_bonus
            ucb_values.append(ucb)
        
        return np.argmax(ucb_values)
    
    def update(self, context, action, reward):
        # Update parameters for chosen action
        self.A[action] += np.outer(context, context)
        self.b[action] += reward * context

# Example: Movie recommendations
class MovieRecommendationEnv:
    def __init__(self, user_features, movie_features, ratings):
        self.user_features = user_features  # (n_users, user_dim)
        self.movie_features = movie_features  # (n_movies, movie_dim)
        self.ratings = ratings  # (n_users, n_movies)
        self.current_user = 0
    
    def reset(self):
        self.current_user = np.random.randint(len(self.user_features))
        return self.get_context()
    
    def get_context(self):
        return self.user_features[self.current_user]
    
    def step(self, movie_id):
        # Reward is actual rating (or click/no-click in real system)
        reward = self.ratings[self.current_user, movie_id]
        
        # Move to next user
        self.current_user = np.random.randint(len(self.user_features))
        context = self.get_context()
        
        return context, reward, False, {}

# Train contextual bandit
env = MovieRecommendationEnv(user_features, movie_features, ratings)
bandit = ContextualBandit(n_actions=len(movie_features), context_dim=user_features.shape[1])

for episode in range(10000):
    context = env.reset()
    action = bandit.choose_action(context)
    next_context, reward, done, _ = env.step(action)
    bandit.update(context, action, reward)
```

---

## Debugging and Common Issues

### Reward Scaling

```python
# Problem: Rewards too large or too small
# Solution: Normalize rewards

class RewardNormalizer:
    def __init__(self, gamma=0.99):
        self.returns = []
        self.gamma = gamma
    
    def normalize(self, reward):
        self.returns.append(reward)
        if len(self.returns) > 1000:
            self.returns.pop(0)
        
        mean = np.mean(self.returns)
        std = np.std(self.returns) + 1e-8
        return (reward - mean) / std
```

### Observation Normalization

```python
from stable_baselines3.common.vec_env import VecNormalize

env = make_vec_env('HalfCheetah-v4', n_envs=4)
env = VecNormalize(env, norm_obs=True, norm_reward=True, clip_obs=10.0)

model = PPO('MlpPolicy', env)
model.learn(total_timesteps=1000000)

# Save normalization statistics
env.save('vec_normalize.pkl')

# Load for evaluation
env = VecNormalize.load('vec_normalize.pkl', env)
env.training = False  # Don't update statistics
env.norm_reward = False  # Don't normalize rewards during evaluation
```

### Hyperparameter Sensitivity

```python
# Common issues and solutions:

# 1. Learning rate too high: Loss explodes
# Solution: Reduce learning rate (1e-4 to 1e-5)

# 2. Discount factor too low: Short-sighted behavior
# Solution: Increase gamma (0.99 or 0.995)

# 3. Exploration too low: Gets stuck in local optimum
# Solution: Increase epsilon or entropy coefficient

# 4. Batch size too small: Unstable training
# Solution: Increase batch size (64 to 256)

# 5. Network too small: Underfitting
# Solution: Increase hidden layer size or add layers
```
