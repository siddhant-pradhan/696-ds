import numpy as np
from collections import defaultdict
from .td import TD


class QLearning(TD):
    def __init__(self, num_actions, gamma, lr):
        self.name = "Q-Learning"
        self.num_actions = num_actions
        self.q_table = defaultdict(lambda: [0.0] * self.num_actions)
        self.gamma = gamma
        self.lr = lr

    def name(self):
        return self.name

    def get_action(self, state):
        #test
        state_ind = state[0][1] * (10) + state[0][0]
        state_test = str(state_ind) + "," + str(state[1])
        qsa = self.q_table[state_test]
        indices = np.where(qsa == np.max(qsa))[0]
        return np.random.choice(indices)

    def train(self, state, action, reward, next_state):
        next_state_ind = next_state[0][1] * (10) + next_state[0][0]
        next_state_test = str(next_state_ind) + "," + str(next_state[1])
        state_ind = state[0][1] * (10) + state[0][0]
        state_test = str(state_ind) + "," + str(state[1])
        next_action = self.get_action(next_state)
        self.q_table[state_test][action] += self.lr*(reward + self.gamma*self.q_table\
                [next_state_test][next_action] - self.q_table[state_test][action])

    def get_policy(self):
        #"one" optimal deterministic policy
        policy = {}
        for s in self.q_table:
            policy[s] = np.argmax(self.q_table[s])
        return policy

    def get_q_values(self, state):
        qsa = self.q_table[state]
        return qsa

    def reset(self):
        pass
