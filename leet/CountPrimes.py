def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    for i in range(n):
        if is_prime(i):
            count += 1
    return count


def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(countPrimes(499979))
