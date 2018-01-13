def amazing_number(array):
    N = len(array)
    shift = [0] * N
    for idx, num in enumerate(array):
        if num >= N:
            continue
        elif num <= 0:
            shift[0] += 1
            print(shift)
        elif num > idx:
            shift[idx + 1] += 1
            if num > idx + 1:
                shift[idx + N - num + 1] -= 1
            print(shift)
        else:
            shift[0] += 1
            shift[idx - num + 1] -= 1
            if idx != N - 1:
                shift[idx + 1] += 1
            print(shift)
    total = 0
    index = 0
    max_number = 0
    for idx, s in enumerate(shift):
        total += s
        if total > max_number:
            max_number = total
            index = idx
    return index


if __name__ == '__main__':
    array = [0, 1, 2]
    print(amazing_number(array))
    array = [5, 3, 8, 7, 2]
    print(amazing_number(array))
