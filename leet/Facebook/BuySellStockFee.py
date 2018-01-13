def max_profit(prices, fee):
    if not prices:
        return 0
    n = len(prices)
    k = n - 1  # there are at most n - 1 transactions

    transaction = [[0 for _ in range(n)]] * (k + 1)

    for i in range(1, k + 1):
        tempMax = -prices[0]
        for j in range(1, n):
            transaction[i][j] = max(transaction[i][j - 1], prices[j] + tempMax - fee)
            tempMax = max(tempMax, transaction[i - 1][j - 1] - prices[j])

    return transaction[k][n - 1]


print(max_profit([1, 3, 2, 8, 4, 9], 2))
print(max_profit([1, 3, 7, 5, 10, 3], 3))
print(max_profit([9, 8, 7, 1, 2], 3))
print(max_profit([20, 10, 30, 50, 10, 9, 8], 2))

# if __name__ == '__main__':
#     n = 5
#     k = 4
#     transaction = [[0 for _ in range(n)]] * (k + 1)
#     print(transaction)
