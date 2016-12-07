# -*- coding: utf-8 -*-
import random
from abc import ABCMeta, abstractmethod

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


class Bandit(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self):
        pass

    def plot(self):
        s = [self.draw() for _ in range(10000)]
        count, bins, ignored = plt.hist(s, 100, normed=True)
        plt.show()


class BanditNormal(Bandit):
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def draw(self):
        return random.gauss(self.mu, self.sigma)


class BanditBernoulli(Bandit):
    def __init__(self, p):
        self.p = p

    def draw(self):
        if random.random() > self.p:
            return 0.0
        else:
            return 1.0


class BanditUniform(Bandit):
    def __init__(self, p):
        self.p = p

    def draw(self):
        return self.p


class BanditAdversarial(Bandit):
    def __init__(self, p, switch):
        self.p = p
        self.switch = switch
        self.count = 0

    def draw(self):
        self.count += 1
        if self.count < self.switch:
            return self.p
        else:
            return -self.p
