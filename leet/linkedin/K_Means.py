import pandas as pd
import numpy as np


class K_Means:
    def __init__(self, k=3, tolerance=0.0001, max_iterations=500):
        self.k = k
        self.tolerance = tolerance
        self.max_iterations = max_iterations


def Euclidean_distance(feat_one, feat_two):
    squared_distance = 0

    # Assuming correct input to the function where the lengths of two features are the same

    for i in range(len(feat_one)):
        squared_distance += (feat_one[i] - feat_two[i]) ** 2

    return np.sqrt(squared_distance)


if __name__ == '__main__':
    df = pd.read_csv(r'ipl.csv')
    df = df[['one', 'two']]
    # print(df)
    dataset = df.astype(float).values.tolist()
    X = df.values  # returns a numpy array
    print(X)

