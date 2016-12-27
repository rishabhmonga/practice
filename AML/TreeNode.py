import pandas as pd
import numpy as np


class DecisionTreeNode:
    def __init__(self):
        """
        def __init__(self,col=-1,value=None,results=None,tb=None,fb=None):
        self.col=col # column index of criteria being tested
        self.value=value # value necessary to get a true result
        self.results=results # dict of results for a branch, None for everything except endpoints
        self.tb=tb # true decision nodes
        self.fb=fb # false decision nodes
        """

    def split(self, df, attribute, attributevalues):
        result = {}
        result_true = df[df[attribute] >= attributevalues]
        result_false = df[df[attribute] < attributevalues]
        return result_true, result_false

    def classlabelcount(self, data):
        results = {}
        for row in data:
            # The result is the last column
            r = row[0]
            if r not in results: results[r] = 0
            results[r] += 1
        return results

    def entropy(self, class1count, class0count):
        totalcount = class0count + class1count
        from math import log
        return -(class1count / totalcount) * log((class1count / totalcount), 2) - (class0count / totalcount) * log(
            (class0count / totalcount), 2)

    # def findbestattrib(self, columnanmes, dataskeleton):


    def dataskeleton(self, df, columnnames):
        data = dict()
        for attrib in columnnames:
            data[attrib] = self.getvalues(df, attrib)
        return data

    def getvalues(self, df, attrib):
        result = []
        for i in df[attrib]:
            if i not in result:
                result.append(i)
        return result


tree = DecisionTreeNode()
df = pd.read_csv("monks_train.csv")
df.columns = ["class", "a1", "a2", "a3", "a4", "a5", "a6", "id"]
# print(tree.split(df, 'class', 1)[0])
data_true = tree.split(df, 'class', 1)[0]
data_false = tree.split(df, 'class', 1)[1]
data_all = np.append(data_true, data_false)
# print(data_true['class'])
# print(len(data_true['class']))
# len(data_false)
# print(tree.entropy(len(data_true['class']), len(data_false['class'])))
# print(df.columns.aslist())
columnnames = set(df.columns)
columnnames.remove('id')
print(tree.getvalues(df, 'a5'))
print(tree.dataskeleton(df, columnnames))
