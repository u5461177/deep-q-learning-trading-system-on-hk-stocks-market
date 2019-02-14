import random
import environment import Environment


class Agent:
	def __init__(self, environment):
		self.environment = environment

    def produce_state_and_get_action(self, isFirst=False):
        state = self.environment.produce_state(self, isFirst)
        action = self.get_action(state, 1000000)  # use static epsilon for now
        return state, action

    @staticmethod
    def get_epsilon_for_iteration(current_iteration, stable_iteration=1000000, initial_epsilon=1,
                                  end_epsilon=0.1):
        """
        decrease the epsilon linearly from 1 to 0.1 over the first million times, and fixed at 0.1 thereafter
        """
        epsilon = end_epsilon

        if current_iteration <= stable_iteration:
            decrease_per_epsilon = (initial_epsilon - end_epsilon) / stable_iteration
            epsilon = initial_epsilon - current_iteration * decrease_per_epsilon

        return epsilon

    def get_action(self, state, iteration):
        # Choose epsilon based on the iteration
        epsilon = self.get_epsilon_for_iteration(iteration)

        # Choose the action
        if random.random() < epsilon:
			action = environment.get_random_action(self)
        else:
            action = 0
            # action = self.model.predict(state).argmax()
        print(self.__class__.__name__ + ": " + str(action))

        return action