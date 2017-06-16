def distributeCandies(candies):
    """
    :type candies: List[int]
    :rtype: int
    """
    # from collections import Counter
    # candy_types = Counter(candies)
    # bro_count = 0
    # sis_count = sum(candy_types.values())
    # while bro_count < sis_count:
    #     idx = candy_types.most_common()[0][0]
    #     candy_types[idx] -= 1
    #     bro_count += 1
    #     # sis_count = sum(x[0] * x[1] for x in candy_types.items())
    #     sis_count = sum(candy_types.values())
    # sis_type = 0
    # for i in candy_types.items():
    #     if i[1] > 0:
    #         sis_type += 1
    # return sis_type
    return min(len(set(candies)), len(candies)/2)


if __name__ == '__main__':
    print(distributeCandies([1, 1, 2, 3]))
    # print(distributeCandies([1, 1, 2, 2, 3, 3]))
