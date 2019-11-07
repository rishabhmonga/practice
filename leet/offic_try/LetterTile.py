"""
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:

Input: "AAABBC"
Output: 188



Note:

    1 <= tiles.length <= 7
    tiles consists of uppercase English letters.

"""

import collections
import math

'''
This is a mathematical problem.
Get the frequencies of different characters [f_0, f_1, ..., f_n].
For each possible choice of frequency [i_0, i_1, ..., i_n] (0 <= i_k <= f_k, k = 0, 1, ..., n),
the number of distinct sequences is (i_0 + i_1 + ... + i_n)! / ( i_0! * i_1! * ... * i_n!).
'''


def numTilePossibilities(tiles: str) -> int:
    freq = collections.Counter(tiles)
    prod = 1
    for f in freq.values():
        prod *= f + 1
    res = 0
    for i in range(1, prod):
        digits = []
        for f in freq.values():
            digits.append(i % (f + 1))
            i = i // (f + 1)
        tmp = math.factorial(sum(digits))
        for d in digits:
            tmp //= math.factorial(d)
        res += tmp
    return res
