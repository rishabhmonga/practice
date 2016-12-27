def perform(func, *arg1):
    return summing(), subtract()


def summing(a=5, b=4):
    return a + b


def subtract(a=5, b=4):
    return a - b


if __name__ == '__main__':
    print perform(summing, subtract())
