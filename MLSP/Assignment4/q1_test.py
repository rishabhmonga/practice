from scipy.io import loadmat
import numpy as np
from matplotlib import pyplot as plt


mfcc = np.array(loadmat('./data/mfcc.mat')['X'])
mfcc = mfcc.T
sigma = np.array(loadmat('./data/MuSigma.mat')['Sigma'])
sigma = sigma.T
mx = np.array(loadmat('./data/MuSigma.mat')['mX'])
mx = mx.T

mean_piano = mx[0]
mean_clap = mx[1]

sigma_piano = sigma[0]
sigma_clap = sigma[1]

def get_p_matrix(data, sigma, mean):
    n = len(data)

    mat_det = np.linalg.det(sigma)
    det_sqrt = np.sqrt(mat_det)
    first_part = (2 * np.pi) ** (12 / 2)
    first_part *= det_sqrt
    first_part = 1 / first_part

    p = []
    for i in range(n):
        exp_val = np.dot(np.dot((data[i] - mean).T, np.linalg.inv(sigma_piano)), (data[i] - mean))
        exp_val = -exp_val / 2
        p.append(np.exp(exp_val) * first_part)
    return p

p_piano = get_p_matrix(mfcc, sigma_piano, mean_piano)
p_clap = get_p_matrix(mfcc, sigma_clap, mean_clap)

p = np.vstack((p_piano, p_clap))

normalized = []
for i in range(len(p)):
    frames = []
    for j in range(len(p[0])):
        frames.append(p[i][j] / (p[0][j] + p[1][j]))
    normalized.append(frames)
p_curl = np.array(normalized)

# plt.imshow(p_bar)
# plt.show()

T = np.array([[0.9, 0.1],
              [0, 1]])

def max_smooth(p_curl, T):
    p_bar = np.zeros(p_curl.shape)
    p_bar[0][0], p_bar[1][0] = p_curl[0][0], p_curl[1][0]

    for j in range(1, len(p_bar[0])):
        label = np.argmax([p_bar[0][j - 1], p_bar[1][j - 1]])
        p_bar[0][j] = np.multiply(T[label].T, [p_curl[0][j], p_curl[1][j]])[0]
        p_bar[1][j] = np.multiply(T[label].T, [p_curl[0][j], p_curl[1][j]])[1]
    return p_bar


p_bar = max_smooth(p_curl, T)

normalized = []
for i in range(len(p_bar)):
    frames = []
    for j in range(len(p_bar[0])):
        frames.append(p_bar[i][j] / (p_bar[0][j] + p_bar[1][j]))
    normalized.append(frames)
p_bar = np.array(normalized)

plt.imshow(p_bar)
plt.show()


# viterbi algo

p_vit = np.zeros(p_bar.shape)
p_vit[0][0], p_vit[1][0] = p_bar[0][0], p_bar[1][0]
B = np.zeros(p.shape)
B[0][0] = 1 if p_vit[0][0] > p_vit[1][0] else 0
B[1][0] = 1 if p_vit[0][0] < p_vit[1][0] else 0
for j in range(1, len(p_vit[0])):
    # label_paino = np.argmax(np.multiply([p_vit[0][j-1], p_vit[1][j-1]], [T[0][0], T[0][1]]))
    label_paino = np.argmax([p_vit[0][j - 1] * T[0][0], p_vit[1][j - 1] * T[0][1]])

    # p_vit[0][j] = np.multiply(T[label_paino].T, [p_bar[0][j], p_bar[1][j]])[0]
    p_vit[0][j] = T[label_paino][0] * p_vit[label_paino][j - 1] * p_bar[0][j]
    B[0][j] = label_paino

    # label_clap = np.argmax(np.multiply([p_vit[0][j-1], p_vit[1][j-1]], [T[1][0], T[1][1]]))
    label_clap = np.argmax([p_vit[0][j - 1] * T[1][0], p_vit[1][j - 1] * T[1][1]])

    # p_vit[1][j] = np.multiply(T[label_clap].T, [p_bar[0][j], p_bar[1][j]])[1]
    p_vit[1][j] = T[label_clap][1] * p_vit[label_clap][j - 1] * p_bar[1][j]

    B[1][j] = label_clap




normalized = []
for i in range(len(p_vit)):
    frames = []
    for j in range(len(p_vit[0])):
        frames.append(p_vit[i][j] / (p_vit[0][j] + p_vit[1][j]))
    normalized.append(frames)
p_vit = np.array(normalized)


# backtrack

p_fin = np.zeros(p_vit.shape)

for i in range(len(p_vit[0]) - 1, 0, -1):
    label_piano = np.argmax([p_vit[0][i], p_vit[1][i]])
    p_fin[0][i - 1] = B[label_piano][i]

    label_clap = np.argmax([p_vit[0][i], p_vit[1][i]])
    p_fin[1][i - 1] = B[label_clap][i]

# print('P-VIT : ', p_vit)
# print('*******************')
# print('B : ', B)
# print('*******************')

print('P-FIN : ', p_fin)

plt.imshow(p_fin)
plt.show()

