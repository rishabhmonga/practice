def palindrome(s):
	l, r = 0, len(s) - 1
	result = []
	while l < r:
		if s[l] != s[r]:
			return False
		l += 1
		r -= 1
	return True


def findAppends(s):
	if palindrome(s):
		return 0
	return 1 + findAppends(s[1:])

if __name__ == '__main__':
    # print(isPalindrome("A man, a plan, a canal: Panama"))
    # print(isPalindrome("aa"))
    # print(isPalindrome("race a car"))

#	print(palindrome('aa'))
#	print(palindrome('b'))
	print(findAppends("aab"))