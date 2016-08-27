class AddDigitOfANumber:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        total = self.getDigitSum(num)
        while total > 9:
            total = self.getDigitSum(total)
        return total

    @staticmethod
    def getDigitSum(num):
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        return total


result = AddDigitOfANumber()
print(AddDigitOfANumber.addDigits(result, 38))
