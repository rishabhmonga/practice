import pandas as pd


class DecisionTreeNode:
    def __init__(self, data: [], attribidx: None):
        self.data = data  # false decision nodes
        self.attribidx = attribidx

    def dataskeleton(self, df, attributenames):
        data = dict()
        for attrib in attributenames:
            data[attrib] = self.getvalues(df, attrib)
        return data

    def dataindexskeleton(self, data, attribindices):
        skel = dict()
        for attrib in attribindices:
            skel[attrib] = self.getvaluesforindex(data, attrib)
        return skel

    def getvalues(self, df, attrib):
        result = []
        for i in df[attrib]:
            if i not in result:
                result.append(i)
        return result

    def getvaluesforindex(self, data, attrib):
        result = []
        for row in data:
            for i in range(len(row)):
                if i == attrib and row[i] not in result:
                    result.append(row[i])
        return result

    def generatetree(self, data, idxskel):
        if len(data) == 0:
            return DecisionTreeNode()

        current_ent = entropy(data)
        best_gain = 0.0
        best_split = None
        best_attribidx = None
        p_ent_branches = 0.0

        for idx in attributeindecies:
            attribvalues = idxskel.get(idx)
            if idx is not 0:
                branches = split(data, idx, attribvalues)
                for branch in branches:
                    p_ent_branches += float(len(branch)) / len(data) * entropy(branch)
                gain = current_ent - p_ent_branches
                flag = True
                for branch in branches:
                    if len(branch) == 0:
                        flag = False
                if gain > best_gain and flag:
                    best_gain = gain
                    best_split = branches
                    best_attribidx = idx

        if best_gain > 0:
            return DecisionTreeNode(best_split, best_attribidx)
        else:
            return DecisionTreeNode(classlabelcount(data))


def split(data, attributeindex, attributevalues):
    result = {}
    for i in attributevalues:
        result[i] = []
    for val in attributevalues:
        for row in data:
            if row[attributeindex] == val:
                result[val].append(row)
    return result


def classlabelcount(data):
    results = {}
    for row in data:
        # The class label is first column
        r = row[0]
        if r not in results:
            results[r] = 0
        results[r] += 1
    return results


def entropy(data):
    from math import log
    result = classlabelcount(data)
    ent = 0.0
    for r in result.keys():
        p = float(result[r] / len(data))
        ent -= p * (log(p, 2))
    return ent


def infomation_gain(data, idx, skel):
    current_ent = entropy(data)
    p_ent_branches = 0.0
    branches = split(data, idx, skel.get(idx))
    for branch in branches.values():
        p_ent_branches += float(len(branch)) / len(data) * entropy(branch)
    return current_ent - p_ent_branches


df = pd.read_csv("monks-1_train.csv")
df.columns = ["class", "a1", "a2", "a3", "a4", "a5", "a6", "id"]
df2 = df.drop('id', 1)
df2.columns = ["class", "a1", "a2", "a3", "a4", "a5", "a6"]
attribindexdict = {}
for index in range(len(df2.columns)):
    attribindexdict[df2.columns[index]] = index
# attribindexdict = {'class': 0, 'a1': 1, 'a2': 2, 'a3': 3, 'a4': 4, 'a5': 5, 'a6': 6}
attributeindecies = attribindexdict.values()

data = df2.values.tolist()
tree = DecisionTreeNode(data, [])
attributeset = set(df2.columns)
skel = tree.dataskeleton(df2, attributeset)

print('attribs : ', attribindexdict)
print('Entropy : ', entropy(data))
print('classlabelcount : ', classlabelcount(data))
print('Split if class 1 : ', split(data, attribindexdict.get('class'), skel.get('class')).keys())
class_1 = split(data, attribindexdict.get('class'), skel.get('class'))[1]
print('2nd Split : ', split(class_1, attribindexdict.get('a5'), skel.get('a5')).keys())

print('IndexSkel : ', tree.dataindexskeleton(data, attributeindecies))

print('THIS : ', tree.data)
print(infomation_gain(data, 1, tree.dataindexskeleton(data, attributeindecies)))

