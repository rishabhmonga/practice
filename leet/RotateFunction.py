# def maxRotateFunction(A):
#     """
#     :type A: List[int]
#     :rtype: int
#     """
#     if A is None or len(A) == 0:
#         return 0
#     result = []
#     for k in range(len(A)):
#         result.append(rotate(A, k))
#     print(result)
#     return max(result)
#
#
# def rotate(A, k):
#     """
#     :param A: List[int]
#     :param i: int
#     :return: int
#     """
#     arr_sum = 0
#     for i in range(len(A)):
#         if k < len(A):
#             arr_sum += i * A[k]
#             k += 1
#         else:
#             arr_sum += i * A[k - len(A)]
#             k += 1
#     return arr_sum

def maxRotateFunction(A):
    """
    :type A: List[int]
    :rtype: int
    """
    if len(A) == 0:
        return 0
    totalSum = sum(A)
    lMax = 0
    for i in range(len(A)):
        lMax += i * A[i]
    gMax = lMax
    for i in range(len(A) - 1, 0, -1):
        lMax += (totalSum - A[i] * len(A))
        gMax = max(gMax, lMax)
    return gMax


if __name__ == '__main__':
    # A = [4, 3, 2, 6]
    # print(maxRotateFunction(A))
    print(maxRotateFunction(A))
