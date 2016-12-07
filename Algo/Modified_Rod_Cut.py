def cut_rod(p, n, c):
    if n < 1:
        return None
    r = [0 for _ in range(n + 1)]
    s = [0 for _ in range(n + 1)]
    for j in range(1, n + 1):
        q = p[j]
        s[j] = j
        for i in range(1, j):
            if q < p[i] + r[j - i] - c:
                q = p[i] + r[j - i] - c
                s[j] = i
        r[j] = q
    result = []
    while n > 0:
        result.append(s[n])
        n -= s[n]
    return result


if __name__ == '__main__':
    price_list = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print(cut_rod(price_list, 10, 4))
