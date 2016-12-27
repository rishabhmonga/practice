from __future__ import print_function


def fib_dp(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.insert(i, fib[i-1] + fib[i-2])
    print(fib)
    return fib[n]

if __name__ == '__main__':
    print(fib_dp(9))
