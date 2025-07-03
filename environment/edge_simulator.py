import numpy as np

class EdgeEnv:
    def __init__(self):
        self.state_size = 3  # battery, latency, data importance
        self.action_size = 2  # [0: local process, 1: offload]
        self.reset()

    def reset(self):
        self.state = np.random.rand(3)
        return self.state

    def step(self, action):
        battery, latency, importance = self.state
        reward = 0

        if action == 0:  # local
            energy = 0.1 + importance * 0.2
            reward = importance - latency - energy
        else:  # offload
            net_quality = np.random.rand()
            delay = 0.2 / net_quality
            reward = importance * net_quality - delay

        next_state = np.random.rand(3)
        done = np.random.rand() > 0.95
        return next_state, reward, done
