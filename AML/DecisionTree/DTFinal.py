from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd

skeleton = {0: [1, 0], 1: [1, 2, 3], 2: [1, 2, 3], 3: [1, 2], 4: [1, 3, 2], 5: [1, 2, 3, 4], 6: [1, 2]}


def grow_tree(data, depth):
    """
    Generates a tree in the form of a dictionary of a list of a tuple

    The dictionary here consists the level of the tree as the key and the
    corresponding nodes at that level present as a list.

    The list here consists of a tuple containing a pair of parent_id and
    the node. {-1 if no parent}

    :param data:
    :param depth:
    :return:
    """
    depth += 1
    # tree = [[] for i in range(depth)]
    tree = dict((i, []) for i in range(depth))
    root = DecisionTreeNode.build_root(data)
    root.idx = root.get_best_attrib()
    root.set_children()

    tree[0] = [(-1, root)]
    for level, nodes in tree.items():
        if level == depth - 1:
            break
        for node in nodes:
            parent_id, parent = node[0], node[1]
            for n in parent.children:
                n.idx = n.get_best_attrib()
                if n.idx is None:
                    break
                n.set_children()
                tree[level + 1].append((parent.idx, n))
    return tree


def get_best_attrib(root):
    """
    provides the index of the attribute with maximum information gain at this level,
    that is not this node's ancestor
    :return:
    """
    info_gain_dict = {}
    for current_attribute in range(1, len(root.mask)):
        if root.mask[current_attribute] == -1:
            mask_copy = list(root.mask)
            info_gain_dict[current_attribute] = information_gain(root.data, current_attribute, mask_copy)
    return max(info_gain_dict.items(), key=lambda x: x[1])[0]


def filter_data(data, mask):
    """
    Provides a filtered form of data consisting of values that correspond to the
    provided mask.

    Mask is a list of size {feature length + 1}, since it also has class label.
    Each value in it represents the value of the corresponding feature we want to
    filter the data against. A value of -1 signifies a wildcard, meaning, we are
    not interested in the what value that feature takes.

    eg: mask = [-1, -1, 2, -1, -1, -1, -1]
    Means we are want to filter data so that it only has a value of 2 for the 3rd
    feature.

    :param data:
    :param mask:
    :return:
    """
    new_data = list()
    num_true = 0
    for i in mask:
        if i != -1:
            num_true += 1
    for row in data:
        found_true = 0
        for i in range(len(mask)):
            if mask[i] != -1 and row[i] == mask[i]:
                found_true += 1
            if mask[i] == -2:
                found_true += 1
        if found_true == num_true:
            new_data.append(row)
    return new_data


class DecisionTreeNode:
    num_features = 7

    """
    Represents the node of a decision tree.

    Its attributes are :
    idx : index of the feature on which the split needs to take place at this level
    data : the part of data that complies with the rules needed to reach this node
    mask : list of values of features need to reach this node
    children : list of DecisionTreeNode(s) on which the next split will take place
    """

    def __init__(self):

        self.idx = -1
        self.data = []
        self.mask = [-1 for i in range(self.num_features)]
        # self.mask[0] = -1         #mask for class label will always be -1
        self.children = []
        self.parent = None

    def get_best_attrib(self):
        """
        provides the index of the attribute with maximum information gain at this level,
        that is not this node's ancestor
        :return:
        """
        info_gain_dict = {}
        for current_attribute in range(1, len(self.mask)):
            if self.mask[current_attribute] == -1:
                mask_copy = list(self.mask)
                info_gain_dict[current_attribute] = information_gain(self.data, current_attribute, mask_copy)
        if info_gain_dict:
            return max(info_gain_dict.items(), key=lambda x: x[1])[0]
        else:
            return None

    def set_children(self):

        self.children = self.get_children()

    def get_children(self):
        """
        generates a list of empty nodes with data filtered corresponding to each of the
        values of the present node
        :return:
        """
        children = []
        for val in skeleton.get(self.idx):
            new_node = DecisionTreeNode()
            new_node.parent = self
            new_node.mask = list(self.mask)
            new_node.mask[self.idx] = val
            new_node.data = filter_data(self.data, new_node.mask)
            children.append(new_node)
        return children

    @staticmethod
    def build_root(data):
        """
        Builds the root of the tree by the setting the default values for all its attributes
        :param data:
        :return:
        """
        root = DecisionTreeNode()
        root.data = data
        root.mask = [-1 for i in range(DecisionTreeNode.num_features)]
        root.mask[0] = -1
        root.children = []
        return root


def class_label_count(data):
    """
    :param data:
    :return: a dictionary with keys as all possible values of the class label
    and their corresponding values equal to their count in the given data
    """
    result = {}
    for row in data:
        classlabel = row[0]
        if classlabel not in result:
            result[classlabel] = 0
        result[classlabel] += 1
    return result


def select_columns(data, attrib_idx):
    """
    :param data:
    :param attrib_idx:
    :return: a list of lists containing column corresponding to a given attribute
    and the class label in the given data
    """
    result = []
    for row in data:
        result.append([row[0], row[attrib_idx]])
    return result


def entropy(data):
    """
    :param data:
    :return: returns the entropy based if the given data
    """
    from math import log
    result = class_label_count(data)
    ent = 0.0
    for r in result.keys():
        p = float(result[r] / sum(result.values()))
        ent -= p * (log(p, 2))
    return ent


def information_gain(data, attrib_idx, mask):
    """
    :param data:
    :param attrib_idx:
    :param mask:
    :return: the information gain of the given attribute
    """
    counts = {}
    parent_ent = entropy(data)
    for row in data:
        if row[attrib_idx] not in counts:
            counts[row[attrib_idx]] = Counter()
        counts[row[attrib_idx]][row[0]] += 1
    p_ent_branch = 0.0
    parent_class_label_sum = sum(class_label_count(data).values())
    for branch in counts:
        branch_mask = list(mask)
        branch_mask[attrib_idx] = branch
        branch_data = filter_data(data, branch_mask)
        branch_ent = entropy(branch_data)
        p_ent_branch += float(sum(counts[branch].values()) / parent_class_label_sum) * branch_ent
        print(p_ent_branch)
    return parent_ent - p_ent_branch


def print_tree(tree):
    """
    prints a given tree in the form :

        <level>:parent=parent.value => current_node:[mask]

    eg:
        2:6=2 => 3:[-1, -1, -1, -1, -1, 3, 2]

    here the first '2' represents the current level of the tree

    '6' is the parent which when takes a value = 2 reaches the present node '3'

    [-1, -1, -1, -1, -1, 3, 2] : is the mask of the current node, representing the various values
    required by each feature to be able to reach this node
    with '-1' acting as a wildcard

    :param tree:
    :return:
    """
    for level, nodes in tree.items():
        print()
        for node in nodes:
            print("\t %s:%s=%s => %s:%s" % (level, node[0], node[1].mask[node[0]], node[1].idx, node[1].mask))


def get_leaves(tree):
    """
    :param tree:
    :returns: a list of all the leaves of the tree
    """
    depth = len(tree) - 1
    leaves = []
    for parent_id, leaf in tree[depth]:
        leaves.append(leaf)
    return leaves


def confusion_matrix(train, test, depth):
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
    tree = grow_tree(train, depth)
    for row in test:
        pc = predict_class(tree, row)
        rc = row[0]
        if pc == rc and pc == 0:
            true_negatives += 1
        if pc == rc and pc == 0:
            true_positives += 1
        if pc != rc and pc == 0:
            false_negatives += 1
        if pc != rc and pc == 1:
            false_positives += 1
    print("=== Confusion Matrix ===")
    print("TN: %s \t\t\t FP: %s | Actual negatives :%s" % (true_negatives, false_positives, true_negatives + false_positives))
    print("FN: %s \t\t\t TP: %s | Actual positives :%s" % (false_negatives, true_positives, false_negatives + true_positives))
    print("Predicted N: %s\tPredicted P: %s" % (true_negatives + false_negatives, false_positives + true_positives))


def find_child(test_row, root):
    """
    Finds the appropriate child node in the tree given the test row and parent node
    :param test_row:
    :param root:
    :return:
    """
    selected_idx = root[1].idx
    test_value = test_row[selected_idx]
    for child in root[1].children:
        if child.mask[selected_idx] == test_value:
            return selected_idx, child


def match(test_row, leaf):
    """
    Checks if the test row complies with the mask of the leaf node
    :param test_row:
    :param leaf:
    :return:
    """
    num_true = 0
    mask = leaf.mask
    for i in mask:
        if i != -1:
            num_true += 1
    found_true = 0
    for i in range(len(mask)):
        if mask[i] != -1 and test_row[i] == mask[i]:
            found_true += 1
    return found_true == num_true


def predict_class(tree, test_row):
    """
    Predicts the class label value by comparing test row with masks of the leaves using the match method
    :param tree:
    :param test_row:
    :return:
    """
    for leaf in get_leaves(tree):
        if match(test_row, leaf):
            c = Counter(class_label_count(leaf.data))
            if c:
                predicted_label = c.most_common(1)[0][0]
                return predicted_label
            else:
                return None
    return None


def get_accuracy_and_misclassifications(train, test, depth):
    """
    Given the training and the test set and the required depth of the tree this method
    builds a decision tree and uses it to predict and compare values with the test set
    and returns accuracy and misclassification rate
    :param train:
    :param test:
    :param depth:
    :return:
    """
    tree = grow_tree(train, depth)
    answers = Counter()
    for row in test:
        pc = predict_class(tree, row)
        rc = row[0]
        if pc == rc:
            answers["correct"] += 1
        else:
            answers["wrong"] += 1
    return answers["correct"] / sum(answers.values()), answers["wrong"] / sum(answers.values())


def read_data(filename):
    """
    Given the filename with relative path, the method reads the data and removes 'id' column
    :param filename:
    :returns: Data in the form of list of lists
    """
    df = pd.read_csv(filename)
    df.columns = ["class", "a1", "a2", "a3", "a4", "a5", "a6", "id"]
    df_temp = df.drop('id', 1)
    return df_temp.values.tolist()


if __name__ == '__main__':
    data_train1 = read_data("..\monks-1_train.csv")
    data_test1 = read_data("..\monks-1_test.csv")
    data_train2 = read_data("..\monks-2_train.csv")
    data_test2 = read_data("..\monks-2_test.csv")
    data_train3 = read_data("..\monks-3_train.csv")
    data_test3 = read_data("..\monks-3_test.csv")

    acc = []
    for d in range(1, 6):
        tree = grow_tree(data_train1, d)
        print("\nGenerating Decision Tree for Monks1 Test Dataset for depth : ", d)
        print_tree(tree)
        result = get_accuracy_and_misclassifications(data_train1, data_test1, d)
        acc.append(result[0])
        print("Missclassification rate for Monks1 Test Dataset for depth : ", d)
        print(result[1])
        print("Generating Confusion Matrix for Monks1 Test Dataset for depth : ", d)
        confusion_matrix(data_train1, data_test1, d)
    plt.xlabel('Depth')
    plt.ylabel('Accuracy Rate')
    plt.plot(range(1, 6), acc)
    # plt.savefig("monks1.png")
    plt.show()

    acc = []
    for d in range(1, 5):
        tree = grow_tree(data_train2, d)
        print("\nGenerating Decision Tree for Monks2 Test Dataset for depth : ", d)
        print_tree(tree)
        result = get_accuracy_and_misclassifications(data_train2, data_test2, d)
        acc.append(result[0])
        print("Missclassification rate for Monks2 Test Dataset for depth : ", d)
        print(result[1])
        print("Generating Confusion Matrix for Monks2 Test Dataset for depth : ", d)
        confusion_matrix(data_train2, data_test2, d)
    plt.plot(range(1, 5), acc)
    # plt.savefig("monks2.png")
    plt.show()

    acc = []
    for d in range(1, 5):
        tree = grow_tree(data_train3, d)
        print("\nGenerating Decision Tree for Monks3 Test Dataset for depth : ", d)
        print_tree(tree)
        result = get_accuracy_and_misclassifications(data_train3, data_test3, d)
        acc.append(result[0])
        print("Missclassification rate for Monks2 Test Dataset for depth : ", d)
        print(result[1])
        print("Generating Confusion Matrix for Monks3 Test Dataset for depth : ", d)
        confusion_matrix(data_train3, data_test3, d)
    plt.plot(range(1, 5), acc)
    # plt.savefig("monks3.png")
    plt.show()

