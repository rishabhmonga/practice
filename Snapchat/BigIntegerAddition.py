def get_linked_list(num, bucket_size):
    result = []
    i = 0

    while i < len(num):
        curr_bucket = ''
        for _ in range(bucket_size):
            curr_bucket += num[i]
            result.append(int(curr_bucket))
            i += 1
    return curr_bucket



def big_add(num1, num2, bucket_size):
    n = get_linked_list(num1, bucket_size)
    return ''


if __name__ == '__main__':
    # print(big_add('1234', '9999', 2))
    print(get_linked_list('1234567890', 3))