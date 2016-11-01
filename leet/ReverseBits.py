# @param n, an integer
# @return an integer
def reverseBits(n):
    n_binary = "{0:032b}".format(n)
    binary_str = list(str(n_binary))
    j = len(binary_str) - 1
    i = 0
    while i < j:
        temp = binary_str[i]
        binary_str[i] = binary_str[j]
        binary_str[j] = temp
        j -= 1
        i += 1
    return int("".join(binary_str), 2)


if __name__ == '__main__':
    print(reverseBits(1))
