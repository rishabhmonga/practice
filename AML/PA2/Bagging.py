from collections import Counter
from random import randint

from AML.PA2 import DT_PA2
import pandas as pd
import numpy as np


def get_samples(df, sample_count):
    data_sets = []
    for _ in range(sample_count):
        data_sets.append(df.sample(len(df), replace=True))
    return data_sets


def bag(samples, depth):
    forest = []
    for sample in samples:
        tree = DT_PA2.grow_tree(sample.as_matrix(), depth)
        forest.append(tree)
    return forest


def prediction(forest, test_row):
    guesses = Counter()
    for tree in forest:
        p = DT_PA2.predict_class(tree, test_row)
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
    # tree = grow_tree(train, depth)
    for row in test:
        pc = prediction(forest, row)
        rc = row[0]
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


def get_accuracy_and_misclassifications(forest, test):
    """
    Given the training and the test set and the required depth of the tree this method
    builds a decision tree and uses it to predict and compare values with the test set
    and returns accuracy and misclassification rate
    :param train:
    :param test:
    :param depth:
    :return:
    """
    answers = Counter()
    for row in test:
        pc = prediction(forest, row)
        rc = row[0]
        if pc == rc:
            answers["correct"] += 1
        else:
            answers["wrong"] += 1
    return answers["correct"] / sum(answers.values()), answers["wrong"] / sum(answers.values())

if __name__ == '__main__':
    data = pd.read_csv("mushroom_train.csv", header=None)
    data = DT_PA2.read_data(data)
    samples = get_samples(data, 10)
    forest = bag(samples, 5)
    DT_PA2.print_tree(forest[0])
    exit()
    test_df = pd.read_csv("mushroom_test.csv")

    test_datas = get_samples(test_df, 1)
    test_data = DT_PA2.read_data(test_datas[0]).as_matrix()
    test_row = test_data[1]
    print(prediction(forest, test_row))
    confusion_matrix(forest, test_data)
    result = get_accuracy_and_misclassifications(forest, test_data)
    print(result)
    print(result[0] - 0.743287800282619)
