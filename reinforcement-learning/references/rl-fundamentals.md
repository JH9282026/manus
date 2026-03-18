# Reinforcement Learning Fundamentals

Core concepts, mathematical foundations, and tabular methods for reinforcement learning.

---

## Markov Decision Processes (MDPs)

### Formal Definition

An MDP is defined by the tuple (S, A, P, R, γ):

**S** — State space (set of all possible states)

**A** — Action space (set of all possible actions)

**P(s'|s,a)** — Transition probability function: probability of transitioning to state s' when taking action a in state s

**R(s,a,s')** — Reward function: immediate reward received after transition

**γ** — Discount factor (0 ≤ γ ≤ 1): determines importance of future rewards

### Markov Property

The future is independent of the past given the present:

```
P(s_t+1 | s_t, a_t, s_t-1, a_t-1, ..., s_0, a_0) = P(s_t+1 | s_t, a_t)
```

The current state contains all relevant information for decision-making.

### Return and Value Functions

**Return (G_t)** — Cumulative discounted reward from time t:

```
G_t = R_t+1 + γ*R_t+2 + γ²*R_t+3 + ... = Σ_{k=0}^{∞} γ^k * R_t+k+1
```

**State-Value Function V^π(s)** — Expected return starting from state s following policy π:

```
V^π(s) = E_π[G_t | s_t = s] = E_π[Σ_{k=0}^{∞} γ^k * R_t+k+1 | s_t = s]
```

**Action-Value Function Q^π(s,a)** — Expected return starting from state s, taking action a, then following policy π:

```
Q^π(s,a) = E_π[G_t | s_t = s, a_t = a]
```

**Advantage Function A^π(s,a)** — How much better action a is compared to average:

```
A^π(s,a) = Q^π(s,a) - V^π(s)
```

---

## Bellman Equations

### Bellman Expectation Equations

Recursive decomposition of value functions:

**State-Value Function:**
```
V^π(s) = Σ_a π(a|s) * Σ_s' P(s'|s,a) * [R(s,a,s') + γ*V^π(s')]
```

**Action-Value Function:**
```
Q^π(s,a) = Σ_s' P(s'|s,a) * [R(s,a,s') + γ*Σ_a' π(a'|s')*Q^π(s',a')]
```

### Bellman Optimality Equations

Optimal value functions satisfy:

**Optimal State-Value Function:**
```
V*(s) = max_a Σ_s' P(s'|s,a) * [R(s,a,s') + γ*V*(s')]
```

**Optimal Action-Value Function:**
```
Q*(s,a) = Σ_s' P(s'|s,a) * [R(s,a,s') + γ*max_a' Q*(s',a')]
```

**Optimal Policy:**
```
π*(s) = argmax_a Q*(s,a)
```

---

## Dynamic Programming

### Policy Evaluation

Compute V^π for a given policy π:

```python
def policy_evaluation(policy, env, gamma=0.99, theta=1e-6):
    """
    Iteratively compute state-value function for given policy.
    """
    V = np.zeros(env.n_states)
    
    while True:
        delta = 0
        for s in range(env.n_states):
            v = V[s]
            # Bellman expectation backup
            new_v = 0
            for a in range(env.n_actions):
                for s_prime in range(env.n_states):
                    prob = env.transition_prob(s, a, s_prime)
                    reward = env.reward(s, a, s_prime)
                    new_v += policy[s, a] * prob * (reward + gamma * V[s_prime])
            V[s] = new_v
            delta = max(delta, abs(v - V[s]))
        
        if delta < theta:
            break
    
    return V
```

### Policy Improvement

Make policy greedy with respect to current value function:

```python
def policy_improvement(V, env, gamma=0.99):
    """
    Compute greedy policy with respect to value function.
    """
    policy = np.zeros((env.n_states, env.n_actions))
    
    for s in range(env.n_states):
        # Compute Q-values for all actions
        q_values = np.zeros(env.n_actions)
        for a in range(env.n_actions):
            for s_prime in range(env.n_states):
                prob = env.transition_prob(s, a, s_prime)
                reward = env.reward(s, a, s_prime)
                q_values[a] += prob * (reward + gamma * V[s_prime])
        
        # Greedy action selection
        best_action = np.argmax(q_values)
        policy[s, best_action] = 1.0
    
    return policy
```

### Policy Iteration

Alternate between policy evaluation and improvement:

```python
def policy_iteration(env, gamma=0.99, theta=1e-6):
    """
    Find optimal policy through policy iteration.
    """
    # Initialize random policy
    policy = np.ones((env.n_states, env.n_actions)) / env.n_actions
    
    while True:
        # Policy evaluation
        V = policy_evaluation(policy, env, gamma, theta)
        
        # Policy improvement
        new_policy = policy_improvement(V, env, gamma)
        
        # Check convergence
        if np.array_equal(policy, new_policy):
            break
        
        policy = new_policy
    
    return policy, V
```

### Value Iteration

Combine policy evaluation and improvement in single update:

```python
def value_iteration(env, gamma=0.99, theta=1e-6):
    """
    Find optimal value function and policy through value iteration.
    """
    V = np.zeros(env.n_states)
    
    while True:
        delta = 0
        for s in range(env.n_states):
            v = V[s]
            # Bellman optimality backup
            q_values = np.zeros(env.n_actions)
            for a in range(env.n_actions):
                for s_prime in range(env.n_states):
                    prob = env.transition_prob(s, a, s_prime)
                    reward = env.reward(s, a, s_prime)
                    q_values[a] += prob * (reward + gamma * V[s_prime])
            V[s] = np.max(q_values)
            delta = max(delta, abs(v - V[s]))
        
        if delta < theta:
            break
    
    # Extract optimal policy
    policy = policy_improvement(V, env, gamma)
    
    return policy, V
```

---

## Monte Carlo Methods

Learn from complete episodes without model knowledge.

### First-Visit MC Prediction

```python
def first_visit_mc_prediction(policy, env, n_episodes=10000, gamma=0.99):
    """
    Estimate state-value function using first-visit MC.
    """
    V = np.zeros(env.n_states)
    returns = {s: [] for s in range(env.n_states)}
    
    for episode in range(n_episodes):
        # Generate episode
        states, actions, rewards = generate_episode(env, policy)
        
        # Compute returns
        G = 0
        visited = set()
        
        for t in reversed(range(len(states))):
            s = states[t]
            r = rewards[t]
            G = r + gamma * G
            
            # First-visit: only count first occurrence
            if s not in visited:
                returns[s].append(G)
                V[s] = np.mean(returns[s])
                visited.add(s)
    
    return V
```

### Monte Carlo Control with ε-Greedy

```python
def mc_control_epsilon_greedy(env, n_episodes=10000, gamma=0.99, epsilon=0.1):
    """
    Find optimal policy using MC control with ε-greedy exploration.
    """
    Q = np.zeros((env.n_states, env.n_actions))
    returns = {(s, a): [] for s in range(env.n_states) 
               for a in range(env.n_actions)}
    
    for episode in range(n_episodes):
        # Generate episode using ε-greedy policy
        states, actions, rewards = [], [], []
        s = env.reset()
        done = False
        
        while not done:
            # ε-greedy action selection
            if np.random.random() < epsilon:
                a = np.random.randint(env.n_actions)
            else:
                a = np.argmax(Q[s])
            
            s_next, r, done = env.step(a)
            states.append(s)
            actions.append(a)
            rewards.append(r)
            s = s_next
        
        # Update Q-values
        G = 0
        visited = set()
        
        for t in reversed(range(len(states))):
            s, a, r = states[t], actions[t], rewards[t]
            G = r + gamma * G
            
            if (s, a) not in visited:
                returns[(s, a)].append(G)
                Q[s, a] = np.mean(returns[(s, a)])
                visited.add((s, a))
    
    # Extract greedy policy
    policy = np.zeros((env.n_states, env.n_actions))
    for s in range(env.n_states):
        best_action = np.argmax(Q[s])
        policy[s, best_action] = 1.0
    
    return policy, Q
```

---

## Temporal Difference Learning

Learn from incomplete episodes using bootstrapping.

### TD(0) Prediction

```python
def td_prediction(policy, env, n_episodes=1000, alpha=0.1, gamma=0.99):
    """
    Estimate state-value function using TD(0).
    """
    V = np.zeros(env.n_states)
    
    for episode in range(n_episodes):
        s = env.reset()
        done = False
        
        while not done:
            # Select action from policy
            a = np.random.choice(env.n_actions, p=policy[s])
            s_next, r, done = env.step(a)
            
            # TD update
            td_target = r + gamma * V[s_next] * (1 - done)
            td_error = td_target - V[s]
            V[s] += alpha * td_error
            
            s = s_next
    
    return V
```

### SARSA (On-Policy TD Control)

```python
class SARSAAgent:
    def __init__(self, n_states, n_actions, alpha=0.1, gamma=0.99, epsilon=0.1):
        self.Q = np.zeros((n_states, n_actions))
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.n_actions = n_actions
    
    def choose_action(self, state):
        # ε-greedy policy
        if np.random.random() < self.epsilon:
            return np.random.randint(self.n_actions)
        return np.argmax(self.Q[state])
    
    def update(self, s, a, r, s_next, a_next, done):
        # SARSA update: uses actual next action
        td_target = r + self.gamma * self.Q[s_next, a_next] * (1 - done)
        td_error = td_target - self.Q[s, a]
        self.Q[s, a] += self.alpha * td_error
    
    def train(self, env, n_episodes=1000):
        for episode in range(n_episodes):
            s = env.reset()
            a = self.choose_action(s)
            done = False
            
            while not done:
                s_next, r, done = env.step(a)
                a_next = self.choose_action(s_next)
                
                # SARSA update
                self.update(s, a, r, s_next, a_next, done)
                
                s, a = s_next, a_next
```

### Q-Learning (Off-Policy TD Control)

```python
class QLearningAgent:
    def __init__(self, n_states, n_actions, alpha=0.1, gamma=0.99, epsilon=0.1):
        self.Q = np.zeros((n_states, n_actions))
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.n_actions = n_actions
    
    def choose_action(self, state):
        # ε-greedy policy
        if np.random.random() < self.epsilon:
            return np.random.randint(self.n_actions)
        return np.argmax(self.Q[state])
    
    def update(self, s, a, r, s_next, done):
        # Q-learning update: uses max over next actions
        td_target = r + self.gamma * np.max(self.Q[s_next]) * (1 - done)
        td_error = td_target - self.Q[s, a]
        self.Q[s, a] += self.alpha * td_error
    
    def train(self, env, n_episodes=1000):
        for episode in range(n_episodes):
            s = env.reset()
            done = False
            total_reward = 0
            
            while not done:
                a = self.choose_action(s)
                s_next, r, done = env.step(a)
                
                # Q-learning update
                self.update(s, a, r, s_next, done)
                
                s = s_next
                total_reward += r
            
            if episode % 100 == 0:
                print(f"Episode {episode}: Total Reward = {total_reward}")
```

### Expected SARSA

```python
def expected_sarsa_update(self, s, a, r, s_next, done):
    # Expected SARSA: uses expected value over next actions
    policy_probs = np.ones(self.n_actions) * self.epsilon / self.n_actions
    best_action = np.argmax(self.Q[s_next])
    policy_probs[best_action] += 1 - self.epsilon
    
    expected_q = np.sum(policy_probs * self.Q[s_next])
    td_target = r + self.gamma * expected_q * (1 - done)
    td_error = td_target - self.Q[s, a]
    self.Q[s, a] += self.alpha * td_error
```

---

## Exploration Strategies

### ε-Greedy

```python
def epsilon_greedy(Q, state, epsilon):
    if np.random.random() < epsilon:
        return np.random.randint(Q.shape[1])  # Random action
    return np.argmax(Q[state])  # Greedy action
```

### Decaying ε-Greedy

```python
class DecayingEpsilonGreedy:
    def __init__(self, epsilon_start=1.0, epsilon_end=0.01, epsilon_decay=0.995):
        self.epsilon = epsilon_start
        self.epsilon_end = epsilon_end
        self.epsilon_decay = epsilon_decay
    
    def choose_action(self, Q, state):
        if np.random.random() < self.epsilon:
            action = np.random.randint(Q.shape[1])
        else:
            action = np.argmax(Q[state])
        
        # Decay epsilon
        self.epsilon = max(self.epsilon_end, self.epsilon * self.epsilon_decay)
        return action
```

### Softmax / Boltzmann Exploration

```python
def softmax_policy(Q, state, temperature=1.0):
    """
    Sample action proportional to exponentiated Q-values.
    """
    q_values = Q[state]
    exp_q = np.exp((q_values - np.max(q_values)) / temperature)
    probs = exp_q / np.sum(exp_q)
    return np.random.choice(len(q_values), p=probs)
```

### Upper Confidence Bound (UCB)

```python
class UCBExploration:
    def __init__(self, n_states, n_actions, c=2.0):
        self.Q = np.zeros((n_states, n_actions))
        self.N = np.zeros((n_states, n_actions))  # Visit counts
        self.c = c  # Exploration parameter
        self.t = 0  # Total timesteps
    
    def choose_action(self, state):
        self.t += 1
        
        # UCB formula
        ucb_values = self.Q[state] + self.c * np.sqrt(
            np.log(self.t) / (self.N[state] + 1e-8)
        )
        return np.argmax(ucb_values)
    
    def update(self, state, action, reward):
        self.N[state, action] += 1
        alpha = 1.0 / self.N[state, action]
        self.Q[state, action] += alpha * (reward - self.Q[state, action])
```

---

## Eligibility Traces

Bridge between Monte Carlo and TD methods.

### TD(λ)

```python
class TDLambdaAgent:
    def __init__(self, n_states, alpha=0.1, gamma=0.99, lambda_=0.9):
        self.V = np.zeros(n_states)
        self.E = np.zeros(n_states)  # Eligibility traces
        self.alpha = alpha
        self.gamma = gamma
        self.lambda_ = lambda_
    
    def update(self, s, r, s_next, done):
        # TD error
        td_error = r + self.gamma * self.V[s_next] * (1 - done) - self.V[s]
        
        # Update eligibility trace
        self.E[s] += 1  # Accumulating traces
        
        # Update all states proportional to eligibility
        self.V += self.alpha * td_error * self.E
        
        # Decay eligibility traces
        self.E *= self.gamma * self.lambda_
        
        if done:
            self.E = np.zeros_like(self.E)  # Reset traces
```

### SARSA(λ)

```python
class SARSALambdaAgent:
    def __init__(self, n_states, n_actions, alpha=0.1, gamma=0.99, 
                 lambda_=0.9, epsilon=0.1):
        self.Q = np.zeros((n_states, n_actions))
        self.E = np.zeros((n_states, n_actions))  # Eligibility traces
        self.alpha = alpha
        self.gamma = gamma
        self.lambda_ = lambda_
        self.epsilon = epsilon
        self.n_actions = n_actions
    
    def choose_action(self, state):
        if np.random.random() < self.epsilon:
            return np.random.randint(self.n_actions)
        return np.argmax(self.Q[state])
    
    def update(self, s, a, r, s_next, a_next, done):
        # TD error
        td_error = r + self.gamma * self.Q[s_next, a_next] * (1 - done) - self.Q[s, a]
        
        # Update eligibility trace
        self.E[s, a] += 1
        
        # Update all state-action pairs
        self.Q += self.alpha * td_error * self.E
        
        # Decay eligibility traces
        self.E *= self.gamma * self.lambda_
        
        if done:
            self.E = np.zeros_like(self.E)
```

---

## Function Approximation Basics

Extend tabular methods to large/continuous state spaces.

### Linear Function Approximation

```python
class LinearVFA:
    def __init__(self, n_features, alpha=0.01, gamma=0.99):
        self.w = np.zeros(n_features)  # Weight vector
        self.alpha = alpha
        self.gamma = gamma
    
    def value(self, features):
        """Compute V(s) = w^T * features(s)"""
        return np.dot(self.w, features)
    
    def update(self, features, r, next_features, done):
        # TD error
        v = self.value(features)
        v_next = 0 if done else self.value(next_features)
        td_error = r + self.gamma * v_next - v
        
        # Gradient descent update
        self.w += self.alpha * td_error * features
```

### Tile Coding (Feature Engineering)

```python
import numpy as np

class TileCoding:
    def __init__(self, n_tilings=8, n_tiles_per_dim=8, state_bounds=None):
        self.n_tilings = n_tilings
        self.n_tiles_per_dim = n_tiles_per_dim
        self.state_bounds = state_bounds
        self.n_features = n_tilings * (n_tiles_per_dim ** len(state_bounds))
    
    def get_features(self, state):
        """Convert continuous state to binary feature vector."""
        features = np.zeros(self.n_features)
        
        for tiling in range(self.n_tilings):
            # Offset each tiling
            offset = tiling / self.n_tilings
            
            # Discretize state
            indices = []
            for i, (low, high) in enumerate(self.state_bounds):
                tile_width = (high - low) / self.n_tiles_per_dim
                tile_index = int((state[i] - low + offset * tile_width) / tile_width)
                tile_index = np.clip(tile_index, 0, self.n_tiles_per_dim - 1)
                indices.append(tile_index)
            
            # Compute feature index
            feature_idx = tiling * (self.n_tiles_per_dim ** len(state))
            for i, idx in enumerate(indices):
                feature_idx += idx * (self.n_tiles_per_dim ** i)
            
            features[feature_idx] = 1.0
        
        return features
```
