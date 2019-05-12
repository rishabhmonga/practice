import math


def is_prime(num):
    sq_num = int(math.sqrt(num)) + 1
    for i in range(2, sq_num):
        if num % i is 0:
            return False
    return True


def rng(num_list):
    pass


if __name__ == '__main__':
    i = 107
    print(i, is_prime(i))
    # print(isTruncatablePrime('12345'))
