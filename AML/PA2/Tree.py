from collections import Counter
from math import log
import numpy as np

import pandas as pd

LABEL_VAL = 'bruises'
COLUMN_NAMES = ["droppable", "cap-shape", "cap-surface", "cap-color", "bruises", "odor", "gill-attachment",
                "gill-spacing", "gill-size", "gill-color", "stalk-shape", "stalk-root", "stalk-surface-above-ring",
                "stalk-surface-below-ring", "stalk-color-above-ring", "stalk-color-below-ring", "veil-type",
                "veil-color", "ring-number", "ring-type", "spore-print-color", "population", "habitat"]


def class_label_count(data, label=LABEL_VAL):
    """
    :param label:
    :param data:
    :return: a dictionary with keys as all possible values of the class label
    and their corresponding values equal to their count in the given data
    """
    return Counter(data[label])


def entropy(data):
    """
    :param data:
    :return: returns the entropy based if the given data
    """
    result = class_label_count(data)
    ent = 0.0
    denominator = sum(result.values())
    for r in result.keys():
        p = float(result[r]) / denominator
        ent -= p * (log(p, 2))
    return ent


def information_gain(data, attribute, label=LABEL_VAL):
    parent_ent = entropy(data)
    df_denominator = data.groupby(attribute).size().reset_index(name='counts')
    df_numerator = data.groupby([label, attribute]).size().reset_index(name='counts')

    df = df_numerator.merge(df_denominator, on=attribute, how='outer', suffixes=('_n', '_d'))

    df['ent'] = (df['counts_n'] / df['counts_d']) * np.log2((df['counts_n'] / df['counts_d']))

    df = df.groupby(attribute).agg({'ent': sum, 'counts_d': 'max'})

    df['ratio'] = df['counts_d'] / sum(df['counts_d'])
    df['ent'] = df['ent'] * df['ratio']

    return parent_ent + sum(df['ent'])


class DecisionTreeNode(object):
    def __init__(self, label):
        self.label = label
        self.branches = []

    def __str__(self):
        return "N:{0}".format(self.label)


class DecisionTreeBranch(object):
    def __init__(self, attr, attr_val):
        self.attr = attr
        self.attr_val = attr_val
        self.child = None

    def __str__(self):
        return "B:{0}={1}".format(self.attr, self.attr_val)


def select_best_attribute(data, attributes):
    gains = []
    for attr in attributes:
        gains.append((attr, information_gain(data, attr)))
    return max(gains, key=lambda x: x[1])


def grow_tree(examples, attributes, label=LABEL_VAL, max_depth=1, depth=0):
    """
    Create a root node for the tree
    If all examples are positive, Return the single-node tree Root, with label = +.
    If all examples are negative, Return the single-node tree Root, with label = -.
    If number of predicting attributes is empty, then Return the single node tree Root,
    with label = most common value of the target attribute in the examples.
    Otherwise Begin
        A ← The Attribute that best classifies examples.
        Decision Tree attribute for Root = A.
        For each possible value, vi, of A,
            Add a new tree branch below Root, corresponding to the test A = vi.
            Let Examples(vi) be the subset of examples that have the value vi for A
            If Examples(vi) is empty
                Then below this new branch add a leaf node with label = most common target value in the examples
            Else below this new branch add the subtree ID3 (Examples(vi), Target_Attribute, Attributes – {A})
    End
    Return Root

    --from wikipedia
    """

    counts = class_label_count(examples)
    # print("Depth={0} counts = {1}".format(depth, counts))
    most_common = counts.most_common(1)[0]

    if len(counts) == 1:
        pure_val = list(counts.keys())[0]
        # print("Depth={0} PURITY adding {1}".format(depth, pure_val))
        return DecisionTreeNode(pure_val)

    if len(attributes) == 0:
        # print("Depth={0} used all attributes {1}".format(depth, most_common))
        return DecisionTreeNode(most_common[0])

    attr, attr_gain = select_best_attribute(examples, attributes)
    # print("Depth={0} selected {1} with {2}".format(depth, attr, attr_gain))
    root = DecisionTreeNode(attr)

    for attr_val in examples[attr].unique():
        # print("Depth={0} Added branch {1}={2}".format(depth, attr, attr_val))
        branch = DecisionTreeBranch(attr, attr_val)
        br_eg = examples[examples[attr] == attr_val]
        if len(br_eg) == 0:
            # print("Depth={0} filtered everything, adding {1}".format(depth, most_common))
            branch.child = DecisionTreeNode(most_common[0])
        elif depth == max_depth:
            # print("Depth={0} max depth reached, adding most_common {1}".format(attr, most_common))
            branch.child = DecisionTreeNode(most_common[0])
        else:
            # make a copy and remove selected attribute
            new_attributes = list(attributes)
            new_attributes.remove(attr)
            branch.child = grow_tree(br_eg, new_attributes, label=label, max_depth=max_depth, depth=depth + 1)
        root.branches.append(branch)
    return root


def print_tree(root, level=1):
    if not root:
        return
    print("\t" * (level - 1), "({0})".format(level), root)
    for r in root.branches:
        print("\t" * level, "--->", r)
        print_tree(r.child, level + 1)


def predict_class(tree, row):
    root = tree
    i = 0
    while True:
        if not root.branches:
            return root.label
        attr, attr_val = root, row[root.label]
        # print(attr, attr_val)
        for b in root.branches:
            if b.attr_val == attr_val:
                break
        root = b.child
        i += 1


def confusion_matrix(tree, test):
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
        pc = predict_class(tree, row)
        rc = row[LABEL_VAL]
        if pc == rc and pc == 'f':
            true_negatives += 1
        if pc == rc and pc == 't':
            true_positives += 1
        if pc != rc and pc == 'f':
            false_negatives += 1
        if pc != rc and pc == 't':
            false_positives += 1
    print("=== Confusion Matrix ===")
    print("TN: %s \t\t\t FP: %s | Actual negatives :%s" % (
        true_negatives, false_positives, true_negatives + false_positives))
    print("FN: %s \t\t\t TP: %s | Actual positives :%s" % (
        false_negatives, true_positives, false_negatives + true_positives))
    print("Predicted N: %s\tPredicted P: %s" % (true_negatives + false_negatives, false_positives + true_positives))


if __name__ == '__main__':
    df = pd.read_csv("mushroom_data.csv", header=None, names=COLUMN_NAMES)
    msk = np.random.rand(len(df)) < 0.8

    df_train = df[msk]
    df_test = df[~msk]

    print("Labels Train:", class_label_count(df_train))
    print("Labels Test:", class_label_count(df_test))

    attributes = list(COLUMN_NAMES)
    attributes.remove(LABEL_VAL)
    attributes.remove('droppable')
    print(attributes)

    print(select_best_attribute(df_train, attributes))

    tree = grow_tree(df_train, attributes, max_depth=5)
    print_tree(tree)
    print("*" * 50)
    confusion_matrix(tree, df_test)
