import sys


def find_greed_quotient(input_list):
    """
    :param input_list:
    :returns: Greed Quotient of a given list
             -1 is GQ is not possible
    """
    input_list.sort()
    N = len(input_list)
    quotient = []
    for i in range(N):
        if (input_list[i] >= N - i) and __check_remaining(input_list, N - i):
            quotient.append(N - i)
    return max(quotient) if len(quotient) != 0 else -1


def __check_remaining(input_list, quotient):
    """
    checks the N-GQ condition
    :param input_list:
    :param quotient:
    :return:
    """
    remaining = 0
    for i in input_list:
        if i < quotient:
            remaining += 1
    if remaining == len(input_list) - quotient:
        return True
    return False


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SyntaxError("Please enter <size of input> \"<list of numbers>\" \n"
                          "eg : python GreedQuotient.py 5 \"[1, 2, 3, 4, 5]\"")
    input_list = eval(sys.argv[2])
    N = eval(sys.argv[1])
    if len(input_list) != N:
        raise ValueError("Size of Input does not match the input length")
    print(find_greed_quotient(input_list))
