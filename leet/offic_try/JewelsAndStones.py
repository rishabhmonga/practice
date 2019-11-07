def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    count = 0
    for s in S:
        if s in J:
            count += 1
    return count


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    # o/p 3

    print(numJewelsInStones(J, S))

    J = "z"
    S = "ZZ"
    # o/p 0

    print(numJewelsInStones(J, S))
