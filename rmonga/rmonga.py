#! /usr/bin/python

'''
This is a template outlining the functions we are expecting for us to be able to
interface with an call your code. This is not all of the functions you need. You
will also need to make sure to bring your decision tree learner in somehow
either by copying your code into a learn_decision_tree function or by importing
your decision tree code in from the file your wrote for PA#1. You will also need
some functions to handle creating your data bags, computing errors on your tree,
and handling the reweighting of data points.

For building your bags numpy's random module will be helpful.
'''

# This is the only non-native library to python you need
import pandas as pd
import numpy as np
import Adaboost
import Bagging

import sys, os;

LABEL_VAL = 'bruises'
COLUMN_NAMES = ["droppable", "cap-shape", "cap-surface", "cap-color", "bruises", "odor", "gill-attachment",
                "gill-spacing", "gill-size", "gill-color", "stalk-shape", "stalk-root", "stalk-surface-above-ring",
                "stalk-surface-below-ring", "stalk-color-above-ring", "stalk-color-below-ring", "veil-type",
                "veil-color", "ring-number", "ring-type", "spore-print-color", "population", "habitat"]

'''
Function: load_and_split_data(datapath)
datapath: (String) the location of the UCI mushroom data set directory in memory

This function loads the data set. datapath points to a directory holding
agaricuslepiotatest1.csv and agaricuslepiotatrain1.csv. The data from each file
is loaded and returned. All attribute values are nomimal. 30% of the data points
are missing a value for attribute 11 and instead have a value of "?". For the
purpose of these models, all attributes and data points are retained. The "?"
value is treated as its own attribute value.

Two nested lists are returned. The first list represents the training set and
the second list represents the test set.
'''


def load_data(datapath):
    pass


'''
Function: learn_bagged(tdepth, numbags, datapath)
tdepth: (Integer) depths to which to grow the decision trees
numbags: (Integer)the number of bags to use to learn the trees
datapath: (String) the location in memory where the data set is stored

This function will manage coordinating the learning of the bagged ensemble.

Nothing is returned, but the accuracy of the learned ensemble model is printed
to the screen.
'''


def learn_bagged(tdepth, numbags, datapath):
    df_train = pd.read_csv("mushroom_train.csv", header=None, names=COLUMN_NAMES)
    df_test = pd.read_csv("mushroom_test.csv", header=None, names=COLUMN_NAMES)

    attributes = list(COLUMN_NAMES)
    attributes.remove(LABEL_VAL)

    forest = Adaboost.ada_boost(df_train, attributes, iterations=numbags, max_depth=tdepth)
    print("Generating Confusion Matrix for BAGGING for depth : " + str(tdepth) + " and with number of bags : "
          + str(numbags))
    Adaboost.confusion_matrix(forest, df_test)


'''
Function: learn_boosted(tdepth, numtrees, datapath)
tdepth: (Integer) depths to which to grow the decision trees
numtrees: (Integer) the number of boosted trees to learn
datapath: (String) the location in memory where the data set is stored

This function wil manage coordinating the learning of the boosted ensemble.

Nothing is returned, but the accuracy of the learned ensemble model is printed
to the screen.
'''


def learn_boosted(tdepth, numtrees, datapath):
    df_train = pd.read_csv("mushroom_train.csv", header=None, names=COLUMN_NAMES)
    df_test = pd.read_csv("mushroom_test.csv", header=None, names=COLUMN_NAMES)

    attributes = list(COLUMN_NAMES)
    attributes.remove(LABEL_VAL)

    samples = Bagging.get_samples(df_train, numtrees)
    forest = Bagging.bag(samples, attributes, tdepth)

    print("Generating Confusion Matrix for ADABOOST for depth : " + str(tdepth) + " and with number of tree : "
          + str(numtrees))
    Bagging.confusion_matrix(forest, df_test)


if __name__ == "__main__":
    # The arguments to your file will be of the following form:
    # <ensemble_type> <tree_depth> <num_bags/trees> <data_set_path>
    # Ex. bag 3 10 mushrooms
    # Ex. boost 1 10 mushrooms

    # Get the ensemble type
    entype = sys.argv[1]
    # Get the depth of the trees
    tdepth = int(sys.argv[2])
    # Get the number of bags or trees
    nummodels = int(sys.argv[3])
    # Get the location of the data set
    datapath = sys.argv[4]

    # Check which type of ensemble is to be learned
    if entype == "bag":
        # Learned the bagged decision tree ensemble
        learn_bagged(tdepth, nummodels, datapath)
    else:
        # Learned the boosted decision tree ensemble
        learn_boosted(tdepth, nummodels, datapath)
