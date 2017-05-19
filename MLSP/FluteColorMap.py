import matplotlib.pyplot as plt
from scipy.io import loadmat
import seaborn as sns

if __name__ == '__main__':
    A = loadmat('./flute.mat')['X']
    ax = sns.heatmap(A)
    plt.show()