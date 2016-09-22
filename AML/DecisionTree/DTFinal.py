from collections import Counter

import pandas as pd

df = pd.read_csv("..\monks_train.csv")
df.columns = ["class", "a1", "a2", "a3", "a4", "a5", "a6", "id"]
df2 = df.drop('id', 1)
data = df2.values.tolist()
skeleton = {0: [1, 0], 1: [1, 2, 3], 2: [1, 2, 3], 3: [1, 2], 4: [1, 3, 2], 5: [1, 2, 3, 4], 6: [1, 2]}


def grow_tree(data, depth):
    depth += 1
    # tree = [[] for i in range(depth)]
    tree = dict((i, []) for i in range(depth))
    print("Tree : ", tree)
    root = DecisionTreeNode.build_root(data, 7)
    root.idx = root.get_best_attrib()
    root.get_children()

    tree[0] = [(-1, root)]
    for level, nodes in tree.items():
        if level == depth-1:
            break
        for node in nodes:
            parent_id, parent = node[0], node[1]
            print("Parent : ", parent_id, parent.idx, parent.mask)
            for n in parent.children:
                n.idx = n.get_best_attrib()
                n.get_children()
                print("\t n : ", n.idx, n.mask)
                tree[level + 1].append((parent.idx, n))
    return tree


def filter_data(data, mask):
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
    def __init__(self):
        self.idx = -1
        self.data = []
        self.mask = []
        self.children = []

    def get_best_attrib(self):
        info_gain_dict = {}
        for current_attribute in range(1, len(self.mask)):
            if self.mask[current_attribute] == -1:
                mask_copy = list(self.mask)
                info_gain_dict[current_attribute] = information_gain(data, current_attribute, mask_copy)
        return max(info_gain_dict.items(), key=lambda x: x[1])[0]

    def get_children(self):
        for val in skeleton.get(self.idx):
            new_node = DecisionTreeNode()
            new_node.mask = list(self.mask)
            new_node.mask[self.idx] = val
            new_node.data = filter_data(self.data, new_node.mask)
            # print(val, new_node.mask)
            # print(val, new_node.data)
            self.children.append(new_node)

    @staticmethod
    def build_root(data, num_features):
        root = DecisionTreeNode()
        root.data = data
        root.mask = [-1 for i in range(num_features)]
        root.mask[0] = -1
        root.children = []
        return root


def classlabelcount(data):
    result = {}
    for row in data:
        classlabel = row[0]
        if classlabel not in result:
            result[classlabel] = 0
        result[classlabel] += 1
    return result


def select_columns(data, attrib_idx):
    result = []
    for row in data:
        result.append([row[0], row[attrib_idx]])
    return result


def entropy(data):
    from math import log
    result = classlabelcount(data)
    ent = 0.0
    for r in result.keys():
        p = float(result[r] / sum(result.values()))
        ent -= p * (log(p, 2))
    return ent


def information_gain(data, attrib_idx, mask):
    counts = {}
    parent_ent = entropy(data)
    for row in data:
        if row[attrib_idx] not in counts:
            counts[row[attrib_idx]] = Counter()
        counts[row[attrib_idx]][row[0]] += 1
    p_ent_branch = 0.0
    parent_class_label_sum = sum(classlabelcount(data).values())
    # print(counts)
    for branch in counts:
        branch_mask = list(mask)
        branch_mask[attrib_idx] = branch
        branch_data = filter_data(data, branch_mask)
        branch_ent = entropy(branch_data)
        # print(branch_ent)
        p_ent_branch += float(sum(counts[branch].values()) / parent_class_label_sum) * branch_ent
    return parent_ent - p_ent_branch


def print_tree(tree):
    for level, nodes in tree.items():
        for node in nodes:
            print("\t"*level, node[0], node[1].idx)

if __name__ == '__main__':
    tree = grow_tree(data, 3)
    print('-'*80)
    print_tree(tree)
# print_tree
#     error_rate(tree)
