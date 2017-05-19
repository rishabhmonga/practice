def find_missing(input_list):
    if len(input_list) == 0:
        return "0-99"
    start = end = 0
    result = ''
    for i in range(len(input_list)):
        if input_list[i] != start:
            end = input_list[i] - 1
            if start == end:
                result += str(start) + ","
            else:
                result += str(start) + "-" + str(end) + ","
        start = input_list[i] + 1
    if start != 100:
        end = 99
        if start - 1 == end:
            result += str(end)
        else:
            result += str(start) + "-" + str(end)
    return result

if __name__ == '__main__':
    print find_missing([])
    print find_missing([0])
    print find_missing([3, 5])
