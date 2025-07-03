from environment.edge_simulator import EdgeEnv
from models.dqn_agent import DQNAgent

env = EdgeEnv()
agent = DQNAgent(state_size=env.state_size, action_size=env.action_size)

episodes = 300
for e in range(episodes):
    state = env.reset()
    done = False
    while not done:
        action = agent.act(state)
        next_state, reward, done = env.step(action)
        agent.remember(state, action, reward, next_state, done)
        agent.replay()
        state = next_state

print("Training finished.")
