def perform(func, *arg1):
    return summing(), subtract()


def summing(a=5, b=4):
    return a + b


def subtract(a=5, b=4):
    return a - b


if __name__ == '__main__':
    arr = [1, 1, 2, 3]
    from collections import Counter

    count = Counter(arr)

    print(count)
    print(sum(count))
    print(sum(x[0] * x[1] for x in count.items()))

