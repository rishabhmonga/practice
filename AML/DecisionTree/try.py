from AML.DecisionTree.DTFinal import *


def build_root():
    root = DecisionTreeNode()
    root.data = data
    root.mask = [-1 for i in range(7)]
    root.mask[0] = -1
    root.children = []
    return root


def test_best_attrib():
    root = build_root()
    print(root.get_best_attrib())


# works
def test_entropy():
    print(entropy(data))
    mask = [1, 1, 2, -1, -1, -1, -1]
    new_data = filter_data(data, mask)
    print(class_label_count(new_data))
    print(entropy(new_data))


# works
def test_classlabelcount():
    print(class_label_count(data))
    mask = [-1, 1, 2, -1, -1, -1, -1]
    new_data = filter_data(data, mask)
    print(new_data)
    print(class_label_count(new_data))


def test_select_columns():
    print(len(select_columns(data, 1)))


# works
def test_filter_data():
    mask = [1, 3, -2, 2, -1, -1, -1]
    print(data)
    print(filter_data(data, mask))
    print(len(filter_data(data, mask)))


def test_information_gain():
    mask = [-1, -1, -1, -1, -1, -1, -1]
    data = read_data("../monks-1_train.csv")
    # print("info gain_0: ", information_gain(data, 0, mask))
    print("info gain_1: ", information_gain(data, 1, mask))
    # print("info gain_2: ", information_gain(data, 2, mask))
    # print("info gain 3: ", information_gain(data, 3, mask))
    # print("info gain 4: ", information_gain(data, 4, mask))
    # print("info gain 5: ", information_gain(data, 5, mask))
    # print("info gain 6: ", information_gain(data, 6, mask))
    # test_data = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 2], [1, 2], [1, 2],
    #              [0, 1], [0, 1], [0, 2], [0, 2], [0, 2]]
    #
    # mask = [-1, -1]
    # print("entropy : ", entropy(test_data))
    # print("info gain : ", information_gain(test_data, 1, mask))


def test_grow_tree():
    grow_tree(data, 1)


def test_confusion_matrix():
    tree = grow_tree(data, 0)
    error_rate(tree)
    confusion_matrix(tree)


if __name__ == '__main__':
    # test_best_attrib()
    # test_grow_tree()
    test_information_gain()
    # test_filter_data()
    # test_classlabelcount()
    # test_entropy()
    # test_select_columns()
    # test_confusion_matrix()
