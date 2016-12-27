class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        from collections import Counter
        lowHighMap = Counter()
        if len(prices) > 0:
            high = prices[0]
            low = prices[0]
            for value in prices:
                if low > value:
                    low = value
                    high = value
                elif high < value:
                    high = value
                lowHighMap[low] = high
        maxDiff = 0
        for value in lowHighMap:
            if lowHighMap[value] - value > maxDiff:
                maxDiff = lowHighMap[value] - value
        return maxDiff


soln = Solution()
print(soln.maxProfit([7, 1, 5, 3, 6, 4]))
print(soln.maxProfit([7, 6, 4, 3, 1]))
print(soln.maxProfit([1, 2]))
