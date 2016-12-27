from random import randint
import time
import sys


def generate_input(size, range_start, range_end):
    input_list = list()
    for i in range(0, size):
        input_list.append(randint(range_start, range_end))
    return sorted(input_list)


def insertion_sort(input_list):
    start_time = time.clock()
    if input_list is None or len(input_list) == 1:
        return input_list, time.clock() - start_time
    for i in range(1, len(input_list)):
        key = input_list[i]
        j = i - 1
        while j >= 0 and input_list[j] > key:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = key
    return input_list, time.clock() - start_time


def input_number():
    if len(sys.argv) != 4:
        raise SyntaxError("Please enter <size of input> <start of range> <end of range> \n"
                          "eg : python InsertionSort.py 100 0 100")
    list_size = eval(sys.argv[1])
    range_start = eval(sys.argv[2])
    range_end = eval(sys.argv[3])
    return generate_input(list_size, range_start, range_end)


if __name__ == '__main__':
    input_list = input_number()
    execution_time = 0.0
    print("Input list : ", input_list)
    result = insertion_sort(input_list)
    print("Sorted List : ", result[0])
    print("Execution Time : ", result[1])
