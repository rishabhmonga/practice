import numpy as np
from scipy.io import loadmat

if __name__ == '__main__':
    wiki = loadmat("wiki.mat")['wiki']
    print(wiki)
    print(wiki.shape)
