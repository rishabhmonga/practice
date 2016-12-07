import pandas as pd
import numpy as np
from AML.PA2.Tree import COLUMN_NAMES, grow_tree, print_tree, predict_class, LABEL_VAL
from collections import namedtuple, Counter

Prediction = namedtuple('Prediction', ['idx', 'label', 'prediction'])
WeakLearner = namedtuple('WeakLearner', ['tree', 'alpha'])


def error(weights, predictions):
    numerator = 0
    for p in predictions:
        if p.label != p.prediction:
            numerator += weights[p.idx]
    return numerator / sum(weights)


def alpha(epsilon):
    return 0.5 * np.log((1 - epsilon) / epsilon)


def get_predictions(tree, df):
    ret_val = []
    for r in df.iterrows():
        idx, r = r[0], r[1]
        p = predict_class(tree, r)
        ret_val.append(Prediction(idx, r[LABEL_VAL], p))
    return ret_val


def adjust_weights(predictions, weights, alpha_):
    ret_val = np.copy(weights)

    for p in predictions:
        if p.label == p.prediction:
            ret_val[p.idx] *= np.power(np.e, -alpha_)
        else:
            ret_val[p.idx] *= np.power(np.e, alpha_)
        print(p, weights[p.idx], ret_val[p.idx])

    # L1 norm
    ret_val = ret_val / sum(ret_val)
    return ret_val


def ada_boost(df, attributes, iterations=1, max_depth=3):
    weak_learners = []
    weights = np.ones(len(df)) / len(df)
    for _ in range(iterations):
        # print("weights:", weights)
        df_train = df.sample(n=len(df), weights=weights, replace=True)

        tree = grow_tree(df_train, attributes, max_depth=max_depth)
        print_tree(tree)

        predictions = get_predictions(tree, df_train)

        epsilon_ = error(weights, predictions)

        # print("Epsilon:", epsilon_)

        alpha_ = alpha(epsilon_)
        # print("Alpha:", alpha_)
        weights = adjust_weights(predictions, weights, alpha_)
        # print("Weights:", weights)
        weak_learners.append(WeakLearner(tree, alpha_))
        if epsilon_ == 0:
            break
    return weak_learners


def predict_boosted(forest, row):
    result = Counter()
    for weak_learner in forest:
        tree = weak_learner.tree
        alpha_ = weak_learner.alpha
        p = predict_class(tree, row)
        result[p] += alpha_
    # print(result)
    return result.most_common(1)[0]


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
        pc = predict_boosted(forest, row)[0]
        rc = row[LABEL_VAL]
        if pc == rc and pc == 'f':
            true_negatives += 1
        if pc == rc and pc == 't':
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
    # df = pd.read_csv("mushroom_train.csv")  # , header=None, names=COLUMN_NAMES)

    # df = pd.read_csv("mushroom_data.csv", header=None, names=COLUMN_NAMES)
    # msk = np.random.rand(len(df)) < 0.8
    # df_train = df[msk]
    # df_test = df[~msk]
    # df_train.to_csv("mushroom_train.csv", header=False, index=False)
    # df_test.to_csv("mushroom_test.csv", header=False, index=False)
    # exit()
    df_train = pd.read_csv("mushroom_train.csv", header=None, names=COLUMN_NAMES)
    df_test = pd.read_csv("mushroom_test.csv", header=None, names=COLUMN_NAMES)
    # df = pd.read_csv("mushroom_data.csv", header=None, names=COLUMN_NAMES)

    attributes = list(COLUMN_NAMES)
    attributes.remove(LABEL_VAL)

    # forest = ada_boost(df, list(df.columns)[1:-1], iterations=10)
    forest = ada_boost(df_train, attributes, iterations=1, max_depth=1)
    # print(forest)
    confusion_matrix(forest, df_test)
