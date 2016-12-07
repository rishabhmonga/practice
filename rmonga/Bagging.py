# -*- coding: utf-8 -*-
from collections import Counter

from Tree import COLUMN_NAMES, grow_tree, print_tree, predict_class, LABEL_VAL
import pandas as pd

LABEL_VAL = LABEL_VAL
COLUMN_NAMES = COLUMN_NAMES


def get_samples(df, sample_count):
    data_sets = []
    for _ in range(sample_count):
        data_sets.append(df.sample(len(df), replace=True))
    return data_sets


def bag(samples, attributes, depth):
    forest = []
    for sample in samples:
        tree = grow_tree(sample, attributes, max_depth=depth)
        # print_tree(tree)
        forest.append(tree)
    return forest


def prediction(forest, test_row):
    guesses = Counter()
    for tree in forest:
        p = predict_class(tree, test_row)
        guesses[p] += 1
    return guesses.most_common(1)[0][0]


def confusion_matrix(forest, test):
    """
    prints the confusion matrix
    :param train: training data
    :param test: test data
    :param depth: depth of the tree
    :return:
    """
    true_positives = 0.0
    true_negatives = 0.0
    false_positives = 0.0
    false_negatives = 0.0
    for row in test.iterrows():
        row = row[1]
        pc = prediction(forest, row)
        rc = row[LABEL_VAL]
        if pc == rc and pc == 't':
            true_negatives += 1
        if pc == rc and pc == 'f':
            true_positives += 1
        if pc != rc and pc == 't':
            false_negatives += 1
        if pc != rc and pc == 'f':
            false_positives += 1
    print("=== Confusion Matrix ===")
    print("TN: %s \t\t\t FP: %s | Actual negatives :%s" % (
        true_negatives, false_positives, true_negatives + false_positives))
    print("FN: %s \t\t\t TP: %s | Actual positives :%s" % (
        false_negatives, true_positives, false_negatives + true_positives))
    print("Predicted N: %s\tPredicted P: %s" % (true_negatives + false_negatives, false_positives + true_positives))

if __name__ == '__main__':

    df_train = pd.read_csv("mushroom_train.csv", header=None, names=COLUMN_NAMES)
    df_test = pd.read_csv("mushroom_test.csv", header=None, names=COLUMN_NAMES)

    attributes = list(COLUMN_NAMES)
    attributes.remove(LABEL_VAL)

    samples = get_samples(df_train, 10)
    forest = bag(samples, attributes, 5)

    confusion_matrix(forest, df_test)
