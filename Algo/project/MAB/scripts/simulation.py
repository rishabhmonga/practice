# -*- coding: utf-8 -*-
import csv

from mab import BanditUniform, BanditNormal, BanditAdversarial, BanditBernoulli
from mab.strategies import Deterministic, EpsilonGreedy, Exp3, EpsilonFirst, DeterministicAlternating
import pandas as pd
import numpy as np

# arms = [BanditNormal(0, 1),
#         BanditNormal(0, 1),
#         BanditNormal(0, 1),
#         BanditNormal(0, 1),
#         BanditNormal(5, 1)
#         ]

arms = [BanditAdversarial(1, 500),
        BanditAdversarial(-1, 500)]

# arms = [BanditUniform(1),
#         BanditUniform(2)]

# arms = [BanditBernoulli(0.5),
#         BanditBernoulli(0.8)]

n_arms = len(arms)
deterministic = Deterministic(n_arms)
deterministic_alternating = DeterministicAlternating(n_arms)
epsilon_first = EpsilonFirst(50, n_arms)
epsilon_greedy = EpsilonGreedy(0.9, n_arms)
exp3 = Exp3(0.02, n_arms)

algos = [
    deterministic,
    deterministic_alternating,
    epsilon_first,
    epsilon_greedy,
    exp3
]

data = []
trials = 1000
filename = "result_adversarial_{trials}".format(trials=trials)

for algo in algos:
    for trial in range(trials):
        chosen_arm = algo.select_arm()
        reward = arms[chosen_arm].draw()
        algo.update(chosen_arm, reward)

        data.append({
            'trial': trial,
            'name': algo.name(),
            'regret': algo.regret(),
            'choice': chosen_arm,
            'debug': str(algo)
        }
        )

df = pd.DataFrame(data)
df.to_csv(filename + ".csv", quoting=csv.QUOTE_ALL, index=False)
pivot_df = pd.pivot_table(df, index=['trial'], values=['regret'], columns=['name'])
pivot_df.to_csv(filename + "_formated.csv", quoting=csv.QUOTE_ALL)
