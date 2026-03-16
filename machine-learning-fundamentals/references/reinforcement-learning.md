# Reinforcement Learning

Comprehensive guide to training agents through trial-and-error with reward signals.

---

## Overview

Reinforcement Learning (RL) enables agents to learn optimal behaviors by interacting with an environment and receiving rewards or penalties. Unlike supervised learning, RL doesn't require labeled data; instead, agents discover strategies through exploration and exploitation.

## Core Concepts

### Markov Decision Process (MDP)

RL problems are formalized as MDPs with:
- **States (S)**: All possible situations the agent can be in
- **Actions (A)**: All possible moves the agent can make
- **Transition Function P(s'|s,a)**: Probability of reaching state s' from state s via action a
- **Reward Function R(s,a,s')**: Immediate reward for transition
- **Discount Factor γ**: Weight of future vs immediate rewards (0 < γ ≤ 1)

**Goal**: Find policy π that maximizes expected cumulative discounted reward

### Key Components

**Agent**: The learner and decision-maker
**Environment**: Everything the agent interacts with
**Policy π**: Strategy mapping states to actions (deterministic or stochastic)
**Value Function V(s)**: Expected return starting from state s
**Q-Function Q(s,a)**: Expected return from state s, taking action a
**Reward Signal**: Immediate feedback from environment

### Exploration vs Exploitation

**Exploration**: Try new actions to discover better strategies
**Exploitation**: Use known good actions to maximize reward

**Strategies**:
- ε-greedy: Explore with probability ε, exploit otherwise
- Softmax: Probabilistic action selection based on Q-values
- Upper Confidence Bound (UCB): Balance exploration and exploitation optimally
- Decaying ε: Start with high exploration, gradually exploit more

## Q-Learning

**Concept**: Model-free algorithm that learns Q-values without knowing transition probabilities.

**Update Rule**:
Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') - Q(s,a)]

Where:
- α: Learning rate
- r: Immediate reward
- γ: Discount factor
- max Q(s',a'): Best Q-value in next state

**Algorithm**:
1. Initialize Q-table with zeros or random values
2. For each episode:
   - Start in initial state s
   - While not terminal:
     - Choose action a using ε-greedy policy
     - Take action, observe reward r and next state s'
     - Update Q(s,a) using update rule
     - s ← s'

**Strengths**:
- Simple and effective for discrete state/action spaces
- Guaranteed convergence to optimal policy
- Off-policy learning (can learn from any policy)

**Limitations**:
- Requires discrete states and actions
- Q-table grows exponentially with state/action dimensions
- Slow convergence for large state spaces

**Use Cases**:
- Grid world navigation
- Simple game playing
- Robotics with discrete actions

## SARSA (State-Action-Reward-State-Action)

**Concept**: On-policy alternative to Q-Learning that updates based on actual action taken.

**Update Rule**:
Q(s,a) ← Q(s,a) + α[r + γQ(s',a') - Q(s,a)]

**Difference from Q-Learning**:
- Q-Learning: Uses max Q(s',a') (off-policy)
- SARSA: Uses Q(s',a') for actual next action (on-policy)

**Characteristics**:
- More conservative than Q-Learning
- Better for risky environments
- Learns policy being followed

## Deep Q-Networks (DQN)

**Concept**: Combines Q-Learning with deep neural networks to handle high-dimensional state spaces.

**Key Innovations**:
1. **Experience Replay**: Store transitions in replay buffer, sample random mini-batches for training
   - Breaks correlation between consecutive samples
   - Improves data efficiency
   - Enables mini-batch learning

2. **Target Network**: Separate network for computing target Q-values
   - Stabilizes training
   - Updated periodically from main network
   - Reduces oscillations

**Architecture**:
- Input: State representation (e.g., game pixels)
- Hidden layers: Convolutional or fully connected
- Output: Q-value for each action

**Algorithm**:
1. Initialize replay buffer D and Q-network with random weights
2. Initialize target network with same weights
3. For each episode:
   - Observe initial state s
   - For each timestep:
     - Select action using ε-greedy on Q-network
     - Execute action, observe reward r and next state s'
     - Store transition (s,a,r,s') in D
     - Sample random mini-batch from D
     - Compute target: y = r + γ max Q_target(s',a')
     - Update Q-network to minimize (y - Q(s,a))²
     - Periodically update target network

**Improvements**:
- **Double DQN**: Reduces overestimation by decoupling action selection and evaluation
- **Dueling DQN**: Separate value and advantage streams
- **Prioritized Experience Replay**: Sample important transitions more frequently
- **Rainbow DQN**: Combines multiple improvements

**Use Cases**:
- Atari game playing
- Robotics with visual input
- Autonomous navigation

## Policy Gradient Methods

**Concept**: Directly optimize policy parameters to maximize expected return.

**Advantages over Value-Based Methods**:
- Handle continuous action spaces naturally
- Learn stochastic policies
- Better convergence properties in some domains

### REINFORCE Algorithm

**Concept**: Monte Carlo policy gradient using full episode returns.

**Update Rule**:
θ ← θ + α∇_θ log π_θ(a|s) G_t

Where:
- θ: Policy parameters
- G_t: Return from timestep t
- ∇_θ log π_θ(a|s): Policy gradient

**Algorithm**:
1. Initialize policy parameters θ
2. For each episode:
   - Generate episode following π_θ
   - For each timestep t:
     - Compute return G_t
     - Update θ using policy gradient

**Strengths**:
- Unbiased gradient estimates
- Works with continuous actions
- Learns stochastic policies

**Limitations**:
- High variance (requires many samples)
- Slow convergence
- Only learns from complete episodes

**Variance Reduction**:
- Baseline subtraction: G_t - b(s)
- Advantage function: A(s,a) = Q(s,a) - V(s)

## Actor-Critic Methods

**Concept**: Combine policy gradient (actor) with value function (critic) for lower variance.

**Components**:
- **Actor**: Policy network π_θ(a|s)
- **Critic**: Value network V_φ(s) or Q_φ(s,a)

**Advantages**:
- Lower variance than pure policy gradient
- Can learn online (no need for full episodes)
- More sample-efficient

### A3C (Asynchronous Advantage Actor-Critic)

**Key Features**:
- Multiple parallel agents exploring different parts of environment
- Asynchronous updates to shared parameters
- Uses advantage function for variance reduction

**Advantage Function**:
A(s,a) = r + γV(s') - V(s)

### PPO (Proximal Policy Optimization)

**Concept**: Constrains policy updates to prevent destructive large changes.

**Clipped Objective**:
L(θ) = min(r_t(θ)A_t, clip(r_t(θ), 1-ε, 1+ε)A_t)

Where r_t(θ) = π_θ(a|s) / π_θ_old(a|s)

**Strengths**:
- Simple to implement
- Stable training
- State-of-the-art performance
- Works well across many domains

**Use Cases**:
- Robotics control
- Continuous control tasks
- Multi-agent systems

### DDPG (Deep Deterministic Policy Gradient)

**Concept**: Actor-critic for continuous action spaces using deterministic policies.

**Key Features**:
- Deterministic policy gradient
- Experience replay
- Target networks for both actor and critic
- Ornstein-Uhlenbeck noise for exploration

**Use Cases**:
- Robotic manipulation
- Continuous control (e.g., torque control)
- Autonomous driving

## Model-Based RL

**Concept**: Learn model of environment dynamics, use for planning.

**Approaches**:
- **Dyna-Q**: Combine model-free learning with planning
- **MCTS (Monte Carlo Tree Search)**: Tree-based planning (used in AlphaGo)
- **Model Predictive Control**: Optimize actions over planning horizon

**Advantages**:
- Sample-efficient (can simulate experience)
- Enables planning and lookahead
- Transfers across tasks with same dynamics

**Challenges**:
- Model errors compound over time
- Difficult to learn accurate models for complex environments

## Multi-Agent RL

**Concept**: Multiple agents learning simultaneously in shared environment.

**Challenges**:
- Non-stationary environment (other agents' policies change)
- Credit assignment (which agent caused outcome?)
- Coordination vs competition

**Approaches**:
- Independent learners: Each agent learns independently
- Centralized training, decentralized execution
- Communication protocols between agents

## Practical Implementation Tips

**Environment Design**:
- Shape rewards to guide learning (reward shaping)
- Avoid sparse rewards (provide intermediate feedback)
- Normalize observations and rewards
- Use appropriate discount factor (0.95-0.99 typical)

**Hyperparameter Tuning**:
- Learning rate: 1e-4 to 1e-3 for deep RL
- Batch size: 32-256 for DQN
- Replay buffer size: 10k-1M transitions
- Target network update frequency: Every 1k-10k steps
- ε decay: Start 1.0, decay to 0.01-0.1

**Training Stability**:
- Clip gradients to prevent explosions
- Use batch normalization or layer normalization
- Monitor Q-value distributions
- Track episode returns and success rates
- Use tensorboard for visualization

**Debugging**:
- Test on simple environments first (CartPole, MountainCar)
- Verify random policy performance as baseline
- Check if agent can overfit to single episode
- Monitor gradient magnitudes
- Visualize learned policies

## Common Applications

**Game Playing**:
- Atari games (DQN)
- Board games (AlphaGo, AlphaZero)
- Real-time strategy games

**Robotics**:
- Manipulation and grasping
- Locomotion and navigation
- Assembly tasks

**Autonomous Systems**:
- Self-driving cars
- Drone control
- Traffic signal optimization

**Recommendation Systems**:
- Personalized content delivery
- Ad placement optimization
- Dynamic pricing

**Resource Management**:
- Data center cooling
- Energy grid optimization
- Inventory management

## Frameworks and Libraries

**OpenAI Gym**: Standard RL environment interface
**Stable Baselines3**: High-quality RL algorithm implementations
**RLlib (Ray)**: Scalable RL for production
**TensorFlow Agents**: TensorFlow-based RL library
**PyTorch RL libraries**: TorchRL, Tianshou

## Challenges and Future Directions

**Sample Efficiency**: RL requires many environment interactions
**Sim-to-Real Transfer**: Policies trained in simulation may not work in reality
**Safety and Robustness**: Ensuring safe exploration and reliable policies
**Generalization**: Transferring learned policies to new tasks
**Interpretability**: Understanding what policies have learned
