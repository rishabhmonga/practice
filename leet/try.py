def perform(func, *arg1):
    return summing(), subtract()


def summing(a=5, b=4):
    return a + b


def subtract(a=5, b=4):
    return a - b


if __name__ == '__main__':
    check = [5,.23,412,34,234]
    i = 0
    while i < (len(check)):
        if check[i] == 5:
            del check[i]
            i -= 1
        i += 1
    print(check)
