# Environments and Frameworks

RL environment setup, OpenAI Gym, Stable-Baselines3, custom environments, and multi-agent systems.

---

## OpenAI Gym

### Basic Usage

```python
import gym

# Create environment
env = gym.make('CartPole-v1')

# Environment properties
print(f"Observation space: {env.observation_space}")
print(f"Action space: {env.action_space}")

# Reset environment
state = env.reset()

# Interaction loop
for step in range(1000):
    # Render (optional)
    env.render()
    
    # Choose action (random for demo)
    action = env.action_space.sample()
    
    # Take step
    next_state, reward, done, info = env.step(action)
    
    if done:
        state = env.reset()
    else:
        state = next_state

env.close()
```

### Popular Gym Environments

**Classic Control:**
- `CartPole-v1` — Balance pole on moving cart (discrete, 4D state, 2 actions)
- `MountainCar-v0` — Drive underpowered car up hill (discrete, 2D state, 3 actions)
- `Acrobot-v1` — Swing two-link robot to height (discrete, 6D state, 3 actions)
- `Pendulum-v1` — Swing pendulum upright (continuous, 3D state, 1D action)

**Box2D:**
- `LunarLander-v2` — Land spacecraft safely (discrete, 8D state, 4 actions)
- `LunarLanderContinuous-v2` — Continuous control version
- `BipedalWalker-v3` — Walk bipedal robot (continuous, 24D state, 4D action)
- `CarRacing-v0` — Top-down car racing (continuous, 96x96x3 image, 3D action)

**Atari:**
- `ALE/Pong-v5` — Classic Pong game
- `ALE/Breakout-v5` — Breakout game
- `ALE/SpaceInvaders-v5` — Space Invaders
- Over 50 Atari 2600 games available

**MuJoCo (requires license):**
- `Ant-v4` — Quadruped locomotion
- `HalfCheetah-v4` — 2D running robot
- `Humanoid-v4` — 3D humanoid locomotion
- `Hopper-v4` — One-legged hopping robot

### Wrappers

Modify environment behavior:

```python
import gym
from gym import wrappers

# Monitor wrapper: record episodes
env = gym.make('CartPole-v1')
env = wrappers.Monitor(env, './videos/', force=True)

# Time limit wrapper
env = wrappers.TimeLimit(env, max_episode_steps=500)

# Reward clipping
class ClipRewardWrapper(gym.RewardWrapper):
    def reward(self, reward):
        return np.clip(reward, -1, 1)

env = ClipRewardWrapper(env)

# Frame stacking for Atari
from gym.wrappers import FrameStack
env = FrameStack(env, num_stack=4)

# Observation normalization
class NormalizeObservation(gym.ObservationWrapper):
    def __init__(self, env):
        super().__init__(env)
        self.mean = np.zeros(env.observation_space.shape)
        self.var = np.ones(env.observation_space.shape)
        self.count = 0
    
    def observation(self, obs):
        self.count += 1
        delta = obs - self.mean
        self.mean += delta / self.count
        self.var += delta * (obs - self.mean)
        
        std = np.sqrt(self.var / self.count)
        return (obs - self.mean) / (std + 1e-8)

env = NormalizeObservation(env)
```

### Atari Preprocessing

```python
import gym
from gym.wrappers import AtariPreprocessing, FrameStack

# Standard Atari preprocessing
env = gym.make('ALE/Pong-v5')
env = AtariPreprocessing(
    env,
    noop_max=30,           # Random no-ops at start
    frame_skip=4,          # Repeat action for 4 frames
    screen_size=84,        # Resize to 84x84
    terminal_on_life_loss=True,  # Episode ends on life loss
    grayscale_obs=True,    # Convert to grayscale
    scale_obs=True         # Scale to [0, 1]
)
env = FrameStack(env, 4)   # Stack 4 frames
```

---

## Stable-Baselines3

### Installation

```bash
pip install stable-baselines3[extra]
```

### Training Agents

```python
from stable_baselines3 import PPO, DQN, A2C, SAC, TD3
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy

# Create vectorized environment (parallel training)
env = make_vec_env('CartPole-v1', n_envs=4)

# Train PPO agent
model = PPO(
    'MlpPolicy',           # Policy network type
    env,
    learning_rate=3e-4,
    n_steps=2048,          # Steps per update
    batch_size=64,
    n_epochs=10,
    gamma=0.99,
    gae_lambda=0.95,
    clip_range=0.2,
    verbose=1,
    tensorboard_log='./logs/'
)

model.learn(total_timesteps=100000)

# Save model
model.save('ppo_cartpole')

# Load model
model = PPO.load('ppo_cartpole')

# Evaluate
mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10)
print(f"Mean reward: {mean_reward:.2f} +/- {std_reward:.2f}")

# Test trained agent
obs = env.reset()
for _ in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    if done:
        obs = env.reset()
```

### Algorithm Selection

| Algorithm | Action Space | Sample Efficiency | Stability | Use Case |
|-----------|--------------|-------------------|-----------|----------|
| DQN | Discrete | Medium | Medium | Atari games, discrete control |
| PPO | Both | Medium | High | General purpose, robust |
| A2C | Both | Low | High | Fast training, simple tasks |
| SAC | Continuous | High | High | Robotics, continuous control |
| TD3 | Continuous | High | High | Robotics, alternative to SAC |
| DDPG | Continuous | Medium | Low | Continuous control (use TD3 instead) |

### Custom Policy Networks

```python
import torch
import torch.nn as nn
from stable_baselines3 import PPO
from stable_baselines3.common.torch_layers import BaseFeaturesExtractor

class CustomCNN(BaseFeaturesExtractor):
    def __init__(self, observation_space, features_dim=256):
        super(CustomCNN, self).__init__(observation_space, features_dim)
        
        n_input_channels = observation_space.shape[0]
        self.cnn = nn.Sequential(
            nn.Conv2d(n_input_channels, 32, kernel_size=8, stride=4),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=4, stride=2),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=3, stride=1),
            nn.ReLU(),
            nn.Flatten()
        )
        
        # Compute shape by doing one forward pass
        with torch.no_grad():
            n_flatten = self.cnn(
                torch.as_tensor(observation_space.sample()[None]).float()
            ).shape[1]
        
        self.linear = nn.Sequential(
            nn.Linear(n_flatten, features_dim),
            nn.ReLU()
        )
    
    def forward(self, observations):
        return self.linear(self.cnn(observations))

# Use custom network
policy_kwargs = dict(
    features_extractor_class=CustomCNN,
    features_extractor_kwargs=dict(features_dim=256)
)

model = PPO('CnnPolicy', env, policy_kwargs=policy_kwargs, verbose=1)
```

### Callbacks

```python
from stable_baselines3.common.callbacks import BaseCallback, EvalCallback, CheckpointCallback

class CustomCallback(BaseCallback):
    def __init__(self, verbose=0):
        super(CustomCallback, self).__init__(verbose)
        self.episode_rewards = []
    
    def _on_step(self):
        # Access training variables
        if self.locals.get('dones')[0]:
            episode_reward = self.locals['infos'][0].get('episode', {}).get('r', 0)
            self.episode_rewards.append(episode_reward)
            
            if self.verbose > 0:
                print(f"Episode reward: {episode_reward}")
        
        return True  # Continue training

# Evaluation callback
eval_callback = EvalCallback(
    eval_env,
    best_model_save_path='./logs/best_model',
    log_path='./logs/results',
    eval_freq=10000,
    deterministic=True,
    render=False
)

# Checkpoint callback
checkpoint_callback = CheckpointCallback(
    save_freq=10000,
    save_path='./logs/checkpoints',
    name_prefix='ppo_model'
)

# Train with callbacks
model.learn(
    total_timesteps=100000,
    callback=[CustomCallback(), eval_callback, checkpoint_callback]
)
```

### Hyperparameter Tuning with Optuna

```python
import optuna
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

def objective(trial):
    # Sample hyperparameters
    learning_rate = trial.suggest_loguniform('learning_rate', 1e-5, 1e-3)
    n_steps = trial.suggest_categorical('n_steps', [128, 256, 512, 1024, 2048])
    gamma = trial.suggest_categorical('gamma', [0.9, 0.95, 0.98, 0.99, 0.995])
    gae_lambda = trial.suggest_categorical('gae_lambda', [0.8, 0.9, 0.92, 0.95, 0.98])
    clip_range = trial.suggest_categorical('clip_range', [0.1, 0.2, 0.3, 0.4])
    
    # Create and train model
    model = PPO(
        'MlpPolicy',
        env,
        learning_rate=learning_rate,
        n_steps=n_steps,
        gamma=gamma,
        gae_lambda=gae_lambda,
        clip_range=clip_range,
        verbose=0
    )
    
    model.learn(total_timesteps=50000)
    
    # Evaluate
    mean_reward, _ = evaluate_policy(model, env, n_eval_episodes=10)
    
    return mean_reward

# Run optimization
study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)

print(f"Best hyperparameters: {study.best_params}")
print(f"Best reward: {study.best_value}")
```

---

## Custom Environments

### Creating Custom Gym Environment

```python
import gym
from gym import spaces
import numpy as np

class CustomEnv(gym.Env):
    """Custom Environment following gym interface"""
    metadata = {'render.modes': ['human']}
    
    def __init__(self):
        super(CustomEnv, self).__init__()
        
        # Define action and observation space
        # Example: 4 discrete actions, 10-dimensional continuous state
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(
            low=-np.inf,
            high=np.inf,
            shape=(10,),
            dtype=np.float32
        )
        
        # Initialize state
        self.state = None
        self.steps = 0
        self.max_steps = 200
    
    def reset(self):
        """Reset environment to initial state"""
        self.state = np.random.randn(10).astype(np.float32)
        self.steps = 0
        return self.state
    
    def step(self, action):
        """Execute action and return (observation, reward, done, info)"""
        # Update state based on action
        self.state += np.random.randn(10) * 0.1
        self.steps += 1
        
        # Compute reward
        reward = -np.linalg.norm(self.state)  # Example: minimize state norm
        
        # Check if episode is done
        done = self.steps >= self.max_steps or reward > -0.1
        
        # Additional info
        info = {'steps': self.steps}
        
        return self.state, reward, done, info
    
    def render(self, mode='human'):
        """Render environment (optional)"""
        print(f"Step: {self.steps}, State: {self.state[:3]}...")
    
    def close(self):
        """Clean up resources (optional)"""
        pass

# Register environment
from gym.envs.registration import register

register(
    id='CustomEnv-v0',
    entry_point='__main__:CustomEnv',
    max_episode_steps=200
)

# Use environment
env = gym.make('CustomEnv-v0')
```

### Grid World Example

```python
class GridWorldEnv(gym.Env):
    def __init__(self, grid_size=5):
        super(GridWorldEnv, self).__init__()
        
        self.grid_size = grid_size
        self.action_space = spaces.Discrete(4)  # Up, Down, Left, Right
        self.observation_space = spaces.Box(
            low=0,
            high=grid_size-1,
            shape=(2,),  # (x, y) position
            dtype=np.int32
        )
        
        self.agent_pos = None
        self.goal_pos = np.array([grid_size-1, grid_size-1])
    
    def reset(self):
        self.agent_pos = np.array([0, 0])
        return self.agent_pos.copy()
    
    def step(self, action):
        # Actions: 0=Up, 1=Down, 2=Left, 3=Right
        if action == 0:  # Up
            self.agent_pos[1] = min(self.agent_pos[1] + 1, self.grid_size - 1)
        elif action == 1:  # Down
            self.agent_pos[1] = max(self.agent_pos[1] - 1, 0)
        elif action == 2:  # Left
            self.agent_pos[0] = max(self.agent_pos[0] - 1, 0)
        elif action == 3:  # Right
            self.agent_pos[0] = min(self.agent_pos[0] + 1, self.grid_size - 1)
        
        # Reward: -1 per step, +10 for reaching goal
        done = np.array_equal(self.agent_pos, self.goal_pos)
        reward = 10.0 if done else -1.0
        
        return self.agent_pos.copy(), reward, done, {}
    
    def render(self, mode='human'):
        grid = np.zeros((self.grid_size, self.grid_size), dtype=str)
        grid[:] = '.'
        grid[self.agent_pos[1], self.agent_pos[0]] = 'A'
        grid[self.goal_pos[1], self.goal_pos[0]] = 'G'
        
        print('\n'.join([' '.join(row) for row in grid]))
        print()
```

---

## Multi-Agent Reinforcement Learning

### PettingZoo

```bash
pip install pettingzoo[all]
```

```python
from pettingzoo.mpe import simple_spread_v2

# Create multi-agent environment
env = simple_spread_v2.parallel_env()

# Reset
observations = env.reset()

# Training loop
while env.agents:
    actions = {agent: env.action_space(agent).sample() for agent in env.agents}
    observations, rewards, dones, infos = env.step(actions)

env.close()
```

### Independent Q-Learning

```python
class MultiAgentQLearning:
    def __init__(self, n_agents, n_states, n_actions, lr=0.1, gamma=0.99, epsilon=0.1):
        self.n_agents = n_agents
        self.agents = [
            QLearningAgent(n_states, n_actions, lr, gamma, epsilon)
            for _ in range(n_agents)
        ]
    
    def choose_actions(self, states):
        return [agent.choose_action(state) for agent, state in zip(self.agents, states)]
    
    def update(self, states, actions, rewards, next_states, dones):
        for i, agent in enumerate(self.agents):
            agent.update(states[i], actions[i], rewards[i], next_states[i], dones[i])
```

### Centralized Training, Decentralized Execution (CTDE)

```python
class CTDEAgent:
    def __init__(self, n_agents, state_dim, action_dim):
        # Centralized critic (sees all agents' states)
        self.critic = CentralizedCritic(n_agents * state_dim, n_agents * action_dim)
        
        # Decentralized actors (each sees only own state)
        self.actors = [Actor(state_dim, action_dim) for _ in range(n_agents)]
    
    def choose_actions(self, states):
        # Each actor chooses action independently
        actions = [actor(state) for actor, state in zip(self.actors, states)]
        return actions
    
    def train(self, states, actions, rewards, next_states):
        # Centralized critic uses global information
        global_state = torch.cat(states, dim=-1)
        global_action = torch.cat(actions, dim=-1)
        global_next_state = torch.cat(next_states, dim=-1)
        
        # Update critic
        q_value = self.critic(global_state, global_action)
        # ... (standard critic update)
        
        # Update actors using centralized critic
        for i, actor in enumerate(self.actors):
            # ... (policy gradient using centralized Q-value)
            pass
```

---

## Visualization and Monitoring

### TensorBoard Integration

```python
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter('runs/experiment_1')

for episode in range(1000):
    total_reward = 0
    state = env.reset()
    done = False
    
    while not done:
        action = agent.choose_action(state)
        next_state, reward, done, _ = env.step(action)
        agent.train_step()
        
        total_reward += reward
        state = next_state
    
    # Log metrics
    writer.add_scalar('Reward/Episode', total_reward, episode)
    writer.add_scalar('Epsilon', agent.epsilon, episode)
    
    if episode % 10 == 0:
        writer.add_histogram('Q-values', agent.q_network.parameters(), episode)

writer.close()
```

View with: `tensorboard --logdir=runs`

### Weights & Biases

```python
import wandb

wandb.init(project='rl-project', config={
    'learning_rate': 1e-3,
    'gamma': 0.99,
    'epsilon': 0.1
})

for episode in range(1000):
    # Training code...
    
    wandb.log({
        'episode': episode,
        'reward': total_reward,
        'epsilon': agent.epsilon,
        'loss': loss
    })

wandb.finish()
```

### Recording Videos

```python
from gym.wrappers import RecordVideo

env = gym.make('CartPole-v1')
env = RecordVideo(env, './videos/', episode_trigger=lambda x: x % 10 == 0)

# Train agent...
# Videos saved every 10 episodes
```
