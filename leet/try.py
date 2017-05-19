import numpy as np
from collections import Counter


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def func(x):
    return np.log10(1+(1/x))


if __name__ == '__main__':
<<<<<<< HEAD
    check = [5,.23,412,34,234]
    i = 0
    while i < (len(check)):
        if check[i] == 5:
            del check[i]
            i -= 1
        i += 1
    print(check)
=======
    result = np.random.rand(10)

    print(result)
    age = 0
    for i in range(len(result)):
        age += i*result[i]/100

    print(age)
>>>>>>> remove nth node from last updates
