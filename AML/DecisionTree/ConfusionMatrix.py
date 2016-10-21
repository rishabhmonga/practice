from __future__ import division


# Tv= True Value, Pdv= Predicted Value


def confusion_matrix(Tv, Pdv):
    conf_mat = [[0, 0], [0, 0]]
    # conf_mat[0][0]=True Negative, conf_mat[1][1] =True Positive
    # conf_mat[0][1]=False Positive, conf_mat[1][0]=False Negative
    for i in range(len(Pdv)):
        if Pdv[i] == 0:
            if Pdv[i] == Tv[i]:
                conf_mat[0][0] += 1
            else:
                conf_mat[1][0] += 1
        elif Pdv[i] == 1:
            if Pdv[i] == Tv[i]:
                conf_mat[1][1] += 1
            else:
                conf_mat[0][1] += 1
    accuracy = (conf_mat[0][0] + conf_mat[1][1]) / len(Tv)
    print(accuracy)
    return conf_mat


def print_confusion_matrix(matrix):
    for row in matrix:
        print(row[0], '\t', row[1])


Tv = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
Pdv = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
matrix = confusion_matrix(Tv, Pdv)
print_confusion_matrix(matrix)
