def shortestToChar(S, C):
    """
    :type S: str
    :type C: str
    :rtype: List[int]
    """
    res = [len(S)]*len(S)
    for idx in range(len(S)):
        if S[idx] == C:
            res[idx] = 0
            idy = idx - 1
            while idy >= 0:
                if S[idy] != C:
                    res[idy] = min(idx - idy, res[idy])
                else:
                    break
                idy -= 1
            idy = idx + 1
            while idy < len(S):
                if S[idy] != C:
                    res[idy] = min(idy - idx, res[idy])
                else:
                    break
                idy += 1
    return res


if __name__ == '__main__':

    # Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
    S = "loveleetcode"
    C = 'e'
    print(shortestToChar(S, C))