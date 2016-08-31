class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # HashMap < Character, Integer > dict = new HashMap < Character, Integer > ();
        # char c = 'A';
        # for (int i=1; i <= 26; i++){
        #   dict.put(c, i);
        #   c += 1;
        # }
        #
        # int number = 0;
        # int j = 0;
        # for (int i = s.length() - 1; i >= 0; i--) {
        #   number = number + (dict.get(s.charAt(i)) * (int)Math.pow(26, j));
        #   j++;
        # }
        # return number;
        num = 0
        i = len(s) - 1
        j = 0
        while i >= 0:
            curr = s[i:i-1]
            num += pow(26, j) * (int(curr) - int('A')) + 1
            j += 1
            i -= 1
        return num

result = Solution()
print(result.titleToNumber("A"))
print(result.titleToNumber("AA"))
print(result.titleToNumber("AB"))
