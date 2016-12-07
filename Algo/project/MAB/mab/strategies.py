# -*- coding: utf-8 -*-
import math
import random
from abc import ABCMeta, abstractmethod

import numpy as np


class Strategy(object):
    __metaclass__ = ABCMeta

    def __init__(self, n_arms):
        self.n_arms = n_arms
        self.wins = np.zeros(n_arms)
        self.pulls = np.zeros(n_arms)
        self.values = np.zeros(n_arms)

    def regret(self):
        return (sum(self.pulls) * np.max(np.nan_to_num(self.wins / self.pulls)) -
                sum(self.wins)) / sum(self.pulls)

    @abstractmethod
    def select_arm(self):
        pass

    def update(self, chosen_arm, reward):
        self.pulls[chosen_arm] += 1
        self.wins[chosen_arm] += reward

    def __str__(self):
        return str(self.__dict__)

    def name(self):
        return self.__class__.__name__


class Deterministic(Strategy):
    def select_arm(self):
        if sum(self.pulls) < 1:
            return 1
        else:
            return 0


class DeterministicAlternating(Strategy):
    def select_arm(self):
        return int(sum(self.pulls) % self.n_arms)


class EpsilonFirst(Strategy):
    """
    explore N times and then always choose the best strategy
    """

    def __init__(self, N, n_arms):
        self.N = N
        super(EpsilonFirst, self).__init__(n_arms)

    def select_arm(self):
        selected = None
        if sum(self.pulls) < self.N:
            return np.random.randint(0, len(self.values))
        else:
            selected = np.argmax(self.wins)

        return selected


class EpsilonGreedy(Strategy):
    """
    with epsilon probability choose the best arm
    otherwise, choose a random arm
    """

    def __init__(self, epsilon, n_arms):
        self.epsilon = epsilon
        super(EpsilonGreedy, self).__init__(n_arms)

    def select_arm(self):
        if random.random() < self.epsilon:
            selected = np.argmax(self.values)
        else:
            selected = np.random.randint(0, len(self.values))
        return selected

    def update(self, chosen_arm, reward):
        self.pulls[chosen_arm] += 1

        n = self.pulls[chosen_arm]
        value = self.values[chosen_arm]

        self.values[chosen_arm] = ((n - 1) / float(n)) * value + (1 / float(n)) * reward
        self.wins[chosen_arm] += reward


class Exp3(Strategy):
    """
    choose arms in a weighted
    """

    def __init__(self, gamma, n_arms):
        self.gamma = gamma
        self.weights = np.ones(n_arms)
        super(Exp3, self).__init__(n_arms)

    @staticmethod
    def categorical_draw(probs):
        z = random.random()
        cum_prob = 0.0
        for i in range(len(probs)):
            prob = probs[i]
            cum_prob += prob
            if cum_prob > z:
                return i
        return len(probs) - 1

    def select_arm(self):
        total_weight = sum(self.weights)
        probs = [0.0 for _ in range(self.n_arms)]
        for arm in range(self.n_arms):
            probs[arm] = (1 - self.gamma) * (self.weights[arm] / total_weight)
            probs[arm] += self.gamma * (1.0 / float(self.n_arms))
        return self.categorical_draw(probs)

    def update(self, chosen_arm, reward):
        self.pulls[chosen_arm] += 1
        self.wins[chosen_arm] += reward

        n_arms = len(self.weights)
        total_weight = sum(self.weights)
        probs = [0.0 for _ in range(n_arms)]
        for arm in range(n_arms):
            probs[arm] = (1 - self.gamma) * (self.weights[arm] / total_weight)
            probs[arm] += self.gamma * (1.0 / float(n_arms))

        x = reward / probs[chosen_arm]
        growth_factor = math.exp((self.gamma / n_arms) * x)
        self.weights[chosen_arm] *= growth_factor
