def findComplement(num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            i <<= 1
        print 'i :', i
        print 'i-1 :', bin(i-1)
        return (i-1) ^ num

if __name__ == '__main__':
    print findComplement(5)
