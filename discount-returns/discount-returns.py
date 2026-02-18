import numpy as np

def discount_returns(rewards, gamma):
    rewards = np.array(rewards, dtype=float)
    returns = np.zeros_like(rewards, dtype=float)
    
    running_sum = 0.0
    for t in reversed(range(len(rewards))):
        running_sum = rewards[t] + gamma * running_sum
        returns[t] = running_sum
        
    return returns.tolist()