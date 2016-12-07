# -*- coding: utf-8 -*-
from mab import *


def test_bandit_plot():
    b = BanditNormal(0, 1)
    b.plot()

    # b = Bandit(normal(5, 1))
    # b.plot()
    #
    # b = Bandit(bernoulli(0.1))
    # b.plot()
    #
    # b = Bandit(binomial(1, 0.5))
    # b.plot()
    #
    # b = Bandit(uniform(1, 1))
    # b.plot()


if __name__ == '__main__':
    test_bandit_plot()
