from collections import Counter


def partition_label(inputStr):
    freq_len = len(set(inputStr))
    new_set_flag = False
    result = []
    part_set = set()
    for i in range(len(inputStr)):
        if new_set_flag:
            part_set = set()
            new_set_flag = False
        part_set.add(inputStr[i])
        if len(part_set) == freq_len:
            result.append(i)
            new_set_flag = False

    return result


if __name__ == '__main__':
    print(partition_label("ababcbacadefegdehijhklij"))
