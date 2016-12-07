from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ax = fig.add_subplot(111, projection='3d')
    # x = [-2.2, -2.0, -0.3, 0.1, 0.2, 0.4, 1.6, 1.7, 1.9, 2.0]
    x = [2, 0, 2, 4, 6, 0, 4]
    y = [1, 1, 2, 0, 1, 0, 3]
    z = [1, 1, -1, -1, 1]
    # ax.scatter(x, y, z, marker='o')
    ax.scatter(x, y, marker='o')
    # ax.scatter(z, c='r', marker='C')
    plt.show()
