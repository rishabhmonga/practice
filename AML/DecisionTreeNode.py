from collections import deque
import pandas as pd

df = pd.read_csv("monks_train.csv")
df.columns = ["class", "a1", "a2", "a3", "a4", "a5", "a6", "id"]
df2 = df.drop('id', 1)
data = df2.values.tolist()
attrib_idx = [i for i in range(7)]

used_attribs = [0]


# *************depth************


def growtree(depth, data, idx, used_attribs, data_skel):
    orderednodes = deque()
    auxQueue = deque()
    root_idx = get_best_attribute(data, data_skel, used_attribs)
    root = create_node(root_idx, data_skel, used_attribs)
    orderednodes.append(root)
    # calc info_gain for first parent
    while depth > 0 or len(orderednodes) is not 0:
        current = orderednodes.popleft()
        used_attribs.append(idx)
        best_attrib = get_best_attribute(data, data_skel, used_attribs)
        orderednodes.append(create_node(best_attrib, data_skel, used_attribs))
        depth -= 1


class DecisionTreeNode:
    def __init__(self, idx, skel, used_attribs):
        self.idx = idx
        self.skel = skel
        self.used_attributes = used_attribs
#       self.parent_class


def classlabelcount(data, used_attributes):
    result = {}
    for row in data:
        if row not in used_attributes:
            classlabel = row[0]
            if classlabel not in result:
                result[classlabel] = 0
            result[classlabel] += 1
    return result


def create_node(attribute, data_skel, used_attribs):
    return DecisionTreeNode(attribute, data_skel, used_attribs)


def get_best_attribute(data, data_skel, used_attribs):
    gain_list = []
    for current_idx in range(7):
        if current_idx not in used_attribs:
            gain_list.append(information_gain(data, current_idx, data_skel))
    return max(gain_list)



root.data = data
root.mask = [-1, -1, -1]
root.children = []

root.select_best() -> a1
set root.mask = [1, -1, -1]
for val in skeleton(a1):
	n1 = new Node()
	n1.mask = copy(root.mask)
	n1.data = filter(feature=a1, value=val, data=data)
	# 1. val = 1
	# 2. val = 2
	# 3. val = 3
	root.children.append(n1)