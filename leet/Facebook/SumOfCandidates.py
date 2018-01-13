soln = set()


def printSum(candidates, index, n):
    ans = []
    for i in range(1, n + 1):
        ans.append(candidates[index[i]])
    soln.add(tuple(sorted(ans)))


def solve1(target, sum, candidates, sz, index, n):
    if sum > target:
        return
    if sum == target:
        printSum(candidates, index, n)

    for i in range(index[n], sz):
        index[n + 1] = i
        solve1(target, sum + candidates[i], candidates, sz, index, n + 1)


def solve(target, candidates):
    sz = len(candidates)
    index = [0] * 10000
    solve1(target, 0, candidates, sz, index, 0)
    print(index[:sz])


def get_combinations(candidates, target):
    ans = set()
    i, j = 0, len(candidates) - 1

    for k in range(len(candidates)):
        while i < j:
            if candidates[i] + candidates[j] > target - candidates[k]:
                j -= 1
            elif candidates[i] + candidates[j] < target - candidates[k]:
                i += 1
            else:
                ans.add(tuple([candidates[i], candidates[j], candidates[k]]))
                i += 1
                j -= 1
    return ans


if __name__ == '__main__':
    target = 7
    candidates = [2, 3, 6, 7]

    # print(get_combinations(candidates, target))

    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    solve(target, candidates)
    print(soln)
