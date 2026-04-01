---
name: reinforcement-learning
description: "Implement reinforcement learning algorithms and train agents to learn optimal policies through interaction with environments. Use for developing RL agents, implementing Q-learning and policy gradient methods, training agents in simulated environments, applying deep reinforcement learning (DQN, A3C, PPO), solving sequential decision-making problems, building game-playing AI, robotics control, and autonomous systems."
---

# Reinforcement Learning

Implement reinforcement learning algorithms to train agents that learn optimal behavior through trial-and-error interaction with environments.

## Overview

This skill provides comprehensive guidance on reinforcement learning (RL), covering fundamental concepts, classical algorithms (Q-learning, SARSA), deep RL methods (DQN, A3C, PPO, SAC), environment frameworks (OpenAI Gym, Unity ML-Agents), and practical applications in game playing, robotics, and autonomous systems. RL enables agents to learn optimal policies by maximizing cumulative rewards through exploration and exploitation.

## Quick Start: Algorithm Selection Guide

| Problem Type | Environment | Algorithm | Reference |
|--------------|-------------|-----------|----------|
| Discrete actions, small state space | Tabular (grid world, simple games) | Q-Learning, SARSA | `/references/rl-fundamentals.md` |
| Discrete actions, large state space | High-dimensional (Atari games) | DQN, Rainbow DQN | `/references/algorithms-methods.md` |
| Continuous actions | Robotics, control tasks | DDPG, TD3, SAC | `/references/algorithms-methods.md` |
| Complex policy learning | Any environment | PPO, A3C, TRPO | `/references/algorithms-methods.md` |
| Multi-agent scenarios | Competitive/cooperative games | MADDPG, QMIX | `/references/applications-case-studies.md` |
| Sparse rewards | Exploration-heavy tasks | Curiosity-driven, HER | `/references/algorithms-methods.md` |
| Model-based planning | Sample-efficient learning | World Models, MuZero | `/references/algorithms-methods.md` |

## Core Concepts

### Markov Decision Process (MDP)

RL problems are formalized as MDPs defined by:

**State (s)** — Current situation of the agent in the environment

**Action (a)** — Decision made by the agent

**Reward (r)** — Immediate feedback signal from environment

**Transition Probability P(s'|s,a)** — Probability of reaching state s' from state s after action a

**Policy π(a|s)** — Strategy mapping states to actions (deterministic or stochastic)

**Value Function V(s)** — Expected cumulative reward from state s following policy π

**Q-Function Q(s,a)** — Expected cumulative reward from state s, taking action a, then following policy π

**Discount Factor γ** — Weight for future rewards (0 ≤ γ ≤ 1)

### Bellman Equations

Fundamental recursive relationships:

**Value Function:**
```
V(s) = E[R_t+1 + γ*V(s_t+1) | s_t = s]
```

**Q-Function (Bellman Optimality):**
```
Q*(s,a) = E[r + γ * max_a' Q*(s', a')]
```

These equations form the basis for value iteration and Q-learning algorithms.

### Exploration vs Exploitation

**Exploration** — Try new actions to discover potentially better strategies

**Exploitation** — Use known information to maximize immediate reward

**ε-greedy** — Choose random action with probability ε, best known action with probability 1-ε

**Softmax/Boltzmann** — Sample actions proportional to their estimated values

**Upper Confidence Bound (UCB)** — Balance exploration and exploitation using confidence intervals

**Curiosity-driven** — Intrinsic rewards for visiting novel states

## Classical RL Algorithms

### Q-Learning (Off-Policy TD Control)

```python
import numpy as np

class QLearningAgent:
    def __init__(self, n_states, n_actions, learning_rate=0.1, 
                 discount=0.99, epsilon=0.1):
        self.q_table = np.zeros((n_states, n_actions))
        self.lr = learning_rate
        self.gamma = discount
        self.epsilon = epsilon
    
    def choose_action(self, state):
        # ε-greedy policy
        if np.random.random() < self.epsilon:
            return np.random.randint(self.q_table.shape[1])
        return np.argmax(self.q_table[state])
    
    def update(self, state, action, reward, next_state, done):
        # Q-learning update rule
        current_q = self.q_table[state, action]
        max_next_q = 0 if done else np.max(self.q_table[next_state])
        new_q = current_q + self.lr * (reward + self.gamma * max_next_q - current_q)
        self.q_table[state, action] = new_q
```

**Key Properties:**
- Off-policy: learns optimal policy while following exploratory policy
- Guaranteed convergence to optimal Q* with sufficient exploration
- Works only for discrete, small state-action spaces

### SARSA (On-Policy TD Control)

```python
def sarsa_update(self, state, action, reward, next_state, next_action, done):
    # SARSA uses actual next action, not max
    current_q = self.q_table[state, action]
    next_q = 0 if done else self.q_table[next_state, next_action]
    new_q = current_q + self.lr * (reward + self.gamma * next_q - current_q)
    self.q_table[state, action] = new_q
```

**Difference from Q-Learning:**
- On-policy: learns value of policy being followed
- More conservative in risky environments
- Updates based on actual next action, not maximum

## Deep Reinforcement Learning

### Deep Q-Network (DQN)

Uses neural network to approximate Q-function for high-dimensional state spaces:

```python
import torch
import torch.nn as nn
import torch.optim as optim
from collections import deque
import random

class DQN(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(DQN, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim)
        )
    
    def forward(self, x):
        return self.network(x)

class DQNAgent:
    def __init__(self, state_dim, action_dim, lr=1e-3, gamma=0.99, 
                 epsilon=1.0, epsilon_decay=0.995, epsilon_min=0.01):
        self.action_dim = action_dim
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        
        # Q-network and target network
        self.q_network = DQN(state_dim, action_dim)
        self.target_network = DQN(state_dim, action_dim)
        self.target_network.load_state_dict(self.q_network.state_dict())
        
        self.optimizer = optim.Adam(self.q_network.parameters(), lr=lr)
        self.memory = deque(maxlen=10000)  # Replay buffer
    
    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, self.action_dim - 1)
        
        with torch.no_grad():
            state_tensor = torch.FloatTensor(state).unsqueeze(0)
            q_values = self.q_network(state_tensor)
            return q_values.argmax().item()
    
    def store_transition(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))
    
    def train(self, batch_size=64):
        if len(self.memory) < batch_size:
            return
        
        # Sample mini-batch from replay buffer
        batch = random.sample(self.memory, batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)
        
        states = torch.FloatTensor(states)
        actions = torch.LongTensor(actions)
        rewards = torch.FloatTensor(rewards)
        next_states = torch.FloatTensor(next_states)
        dones = torch.FloatTensor(dones)
        
        # Current Q values
        current_q = self.q_network(states).gather(1, actions.unsqueeze(1))
        
        # Target Q values (using target network)
        with torch.no_grad():
            max_next_q = self.target_network(next_states).max(1)[0]
            target_q = rewards + (1 - dones) * self.gamma * max_next_q
        
        # Compute loss and update
        loss = nn.MSELoss()(current_q.squeeze(), target_q)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        # Decay epsilon
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)
    
    def update_target_network(self):
        self.target_network.load_state_dict(self.q_network.state_dict())
```

**DQN Innovations:**
1. **Experience Replay** — Store transitions in buffer, sample randomly to break correlations
2. **Target Network** — Separate network for computing targets, updated periodically
3. **Frame Stacking** — Use multiple consecutive frames as state (for Atari)

### Policy Gradient Methods

Directly optimize policy π(a|s) instead of learning value function:

**REINFORCE Algorithm:**
```python
class PolicyNetwork(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(PolicyNetwork, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim),
            nn.Softmax(dim=-1)
        )
    
    def forward(self, x):
        return self.network(x)

class REINFORCEAgent:
    def __init__(self, state_dim, action_dim, lr=1e-3, gamma=0.99):
        self.policy = PolicyNetwork(state_dim, action_dim)
        self.optimizer = optim.Adam(self.policy.parameters(), lr=lr)
        self.gamma = gamma
        self.saved_log_probs = []
        self.rewards = []
    
    def choose_action(self, state):
        state_tensor = torch.FloatTensor(state)
        probs = self.policy(state_tensor)
        action_dist = torch.distributions.Categorical(probs)
        action = action_dist.sample()
        self.saved_log_probs.append(action_dist.log_prob(action))
        return action.item()
    
    def train(self):
        # Compute discounted returns
        returns = []
        G = 0
        for r in reversed(self.rewards):
            G = r + self.gamma * G
            returns.insert(0, G)
        
        returns = torch.FloatTensor(returns)
        returns = (returns - returns.mean()) / (returns.std() + 1e-8)  # Normalize
        
        # Compute policy gradient loss
        policy_loss = []
        for log_prob, G in zip(self.saved_log_probs, returns):
            policy_loss.append(-log_prob * G)
        
        policy_loss = torch.stack(policy_loss).sum()
        
        # Update policy
        self.optimizer.zero_grad()
        policy_loss.backward()
        self.optimizer.step()
        
        # Clear episode data
        self.saved_log_probs = []
        self.rewards = []
```

### Actor-Critic Methods

Combine policy gradient (actor) with value function (critic):

**Advantage Actor-Critic (A2C):**
- Actor: policy network π(a|s)
- Critic: value network V(s)
- Advantage: A(s,a) = Q(s,a) - V(s) = r + γV(s') - V(s)

**Proximal Policy Optimization (PPO):**
- Most popular modern RL algorithm
- Clips policy updates to prevent large changes
- Stable, sample-efficient, easy to tune

## Environment Frameworks

### OpenAI Gym

```python
import gym

# Create environment
env = gym.make('CartPole-v1')

# Reset environment
state = env.reset()

# Training loop
for episode in range(1000):
    state = env.reset()
    done = False
    total_reward = 0
    
    while not done:
        # Agent chooses action
        action = agent.choose_action(state)
        
        # Environment step
        next_state, reward, done, info = env.step(action)
        
        # Agent learns
        agent.store_transition(state, action, reward, next_state, done)
        agent.train()
        
        state = next_state
        total_reward += reward
    
    print(f"Episode {episode}: Reward = {total_reward}")

env.close()
```

**Popular Gym Environments:**
- `CartPole-v1` — Balance pole on cart (discrete actions)
- `MountainCar-v0` — Drive car up hill (discrete actions)
- `LunarLander-v2` — Land spacecraft (discrete actions)
- `Pendulum-v1` — Swing pendulum upright (continuous actions)
- `Atari/*` — Atari 2600 games (pixel observations)

### Stable-Baselines3

High-quality RL algorithm implementations:

```python
from stable_baselines3 import PPO, DQN, SAC
from stable_baselines3.common.env_util import make_vec_env

# Create vectorized environment
env = make_vec_env('CartPole-v1', n_envs=4)

# Train PPO agent
model = PPO('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=100000)

# Save model
model.save('ppo_cartpole')

# Load and evaluate
model = PPO.load('ppo_cartpole')
obs = env.reset()
for _ in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    if done:
        obs = env.reset()
```

## Training Best Practices

### Hyperparameter Tuning

**Learning Rate** — Start with 1e-3 to 1e-4, decay over time

**Discount Factor γ** — 0.99 for long-horizon tasks, 0.9-0.95 for shorter tasks

**Exploration (ε)** — Start at 1.0, decay to 0.01-0.1

**Batch Size** — 32-256 for DQN, larger for policy gradient methods

**Replay Buffer Size** — 10k-1M transitions depending on task complexity

**Target Network Update Frequency** — Every 1000-10000 steps for DQN

### Reward Shaping

```python
# Add intermediate rewards to guide learning
def shaped_reward(state, action, next_state, original_reward):
    # Example: reward for moving toward goal
    distance_to_goal = np.linalg.norm(next_state[:2] - goal_position)
    shaped = original_reward - 0.1 * distance_to_goal
    return shaped
```

**Caution:** Improper reward shaping can lead to unintended behavior.

### Curriculum Learning

Gradually increase task difficulty:

```python
# Start with easier version of task
if episode < 100:
    env.set_difficulty('easy')
elif episode < 500:
    env.set_difficulty('medium')
else:
    env.set_difficulty('hard')
```

## Using the Reference Files

### When to Read Each Reference

**`/references/rl-fundamentals.md`** — Read when learning RL basics, understanding MDPs and Bellman equations, implementing tabular methods (Q-learning, SARSA), or working with simple discrete environments.

**`/references/algorithms-methods.md`** — Read when implementing deep RL algorithms (DQN, PPO, SAC), choosing algorithms for specific problems, understanding policy gradient methods, or working with continuous action spaces.

**`/references/environments-frameworks.md`** — Read when setting up RL environments, using OpenAI Gym or custom environments, working with Stable-Baselines3, or implementing multi-agent systems.

**`/references/applications-case-studies.md`** — Read when applying RL to game playing, robotics control, autonomous systems, or real-world problems. Includes case studies and implementation examples.

## References

- [Algorithms Methods](references/algorithms-methods.md)
- [Applications Case Studies](references/applications-case-studies.md)
- [Environments Frameworks](references/environments-frameworks.md)
- [Rl Fundamentals](references/rl-fundamentals.md)
