def min_coins_top_down(coins, total, memo):
    """
    T[i] = min(T[i], 1 + T[i - coins[j]])

    :param coins: list()
    :param total: int
    :param memo: dict()
    :return: int
    """
    if total == 0:
        return 0

    if total in memo:
        return memo[total]

    min_value = float("inf")
    for i in range(len(coins)):
        coin = coins[i]
        if coin > total:
            continue
        val = min_coins_top_down(coins, total - coin, memo)
        min_value = min(min_value, val)

    min_value += 1

    memo[total] = min_value
    return min_value


if __name__ == '__main__':
    coins = [1, 5, 6, 8]
    total = 11
    expected = 2

    # assert expected == min_coins_top_down(coins, total, dict())
    memoize = dict()
    assert expected == min_coins_top_down(coins, total, memoize)

    print(memoize)
