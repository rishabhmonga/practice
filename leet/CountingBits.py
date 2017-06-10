def countBits2(num):
        """
        :type num: int
        :rtype: List[int]
        """
        offset = 1
        bits = [0 for _ in range(num+1)]
        for idx in range(1, num+1):
            if offset * 2 == idx:
                offset *= 2
            bits[idx] = bits[idx - offset] + 1
        return bits

def countBits(num):
    bits = [0 for _ in range(num+1)]

    # Recurrance:  f[i] = f[i / 2] + i % 2
    for idx in range(1, num+1):
        bits[idx] = bits[idx >> 1] + (idx & 1)

    return bits

if __name__ == '__main__':
    print countBits(5)
    print countBits2(5)
