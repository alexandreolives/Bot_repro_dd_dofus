import tensorflow as tf
import random
import numpy as np
from tensorflow.keras import layers
from collections import deque
from gym import spaces

class Environnement(gym.Env):
    def __init__(self):
        super(Environnement, self).__init__()
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(low=0, high=1, shape=(10,), dtype=np.float32)  # Exemple: état de 10 dimensions
        self.state = self.reset()
        self.generation = 0
        self.max_generations = 10

    def get_generation(self) :
        return self.generation

    def set_generation(self, actual_generation) :
        self.generation = actual_generation
    
    def step(self, action):
        assert self.action_space.contains(action)
        reward = 0
        done = False

        # Simulez le croisement ici, mettez à jour self.state et reward
        if action > self.generation:
            reward = 1000
            self.generation += 1

        elif action == self.generation:
            reward = 1

        elif action < self.generation-2 :
            reward = -1000

        if self.generation == self.max_generations:
            done = True

        return np.array(self.state), reward, done, {}

    def reset(self):
        self.state = np.random.rand(10)
        self.generation = 0
        return np.array(self.state)

    def render(self):
        print(f"Generation: {self.generation}, State: {self.state}")

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95  # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model = self._build_model()

    def _build_model(self):
        model = tf.keras.Sequential()
        model.add(layers.Dense(64, input_dim=self.state_size, activation='relu'))
        model.add(layers.Dense(32, input_dim=self.state_size, activation='relu'))
        model.add(layers.Dense(16, activation='relu'))
        model.add(layers.Dense(self.action_size, activation='linear'))
        model.compile(optimizer=tf.keras.optimizers.Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = (reward + self.gamma * np.amax(self.model.predict(next_state)[0]))
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)
