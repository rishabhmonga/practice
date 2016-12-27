from random import randint
import time
import sys


def generate_input(size, range_start, range_end):
    input_list = list()
    for i in range(0, size):
        input_list.append(randint(range_start, range_end))
    return input_list


def input_number():
    if len(sys.argv) != 4:
        raise SyntaxError("Please enter <size of input> <start of range> <end of range> \n"
                          "eg : python InsertionSort.py 100 0 100")
    list_size = eval(sys.argv[1])
    range_start = eval(sys.argv[2])
    range_end = eval(sys.argv[3])
    return generate_input(list_size, range_start, range_end)


class QuickSort:
    @staticmethod
    def __partition(input_list, low, high):
        pivot = input_list[high]
        i = low
        for j in range(low, high):
            if input_list[j] <= pivot:
                temp = input_list[i]
                input_list[i] = input_list[j]
                input_list[j] = temp
                i += 1
        temp = input_list[i]
        input_list[i] = input_list[high]
        input_list[high] = temp
        return i

    @staticmethod
    def __quick_sort(input_list, low, high):
        if low < high:
            partition = QuickSort.__partition(input_list, low, high)
            QuickSort.__quick_sort(input_list, low, partition - 1)
            QuickSort.__quick_sort(input_list, partition + 1, high)

    @staticmethod
    def sort(input_list):
        start_time = time.clock()
        QuickSort.__quick_sort(input_list, 0, len(input_list) - 1)
        return input_list, time.clock() - start_time


if __name__ == '__main__':
    input_list = input_number()
    execution_time = 0.0
    print("Input list : ", input_list)
    result = QuickSort.sort(input_list)
    print("Sorted List : ", result[0])
    print("Execution Time : ", result[1])
