"""
int len = 1;
long count = 9;
int start = 1;

while (n > len * count) {
	n -= len * count;
	len += 1;
	count *= 10;
   	start *= 10;
}
start += (n - 1) / len;
String s = Integer.toString(start);
return Character.getNumericValue(s.charAt((n - 1) % len));
"""


def findNthDigit(n):
    """
    :type n: int
    :rtype: int
    """
    length = 1
    count = 9
    start = 1

    while n > length*count:
        n -= length * count
        length += 1
        count *= 10
        start *= 10
    start += (n-1) / length
    s = str(start)
    return int(s[(n-1) % length])


if __name__ == '__main__':
    print(findNthDigit(9))
