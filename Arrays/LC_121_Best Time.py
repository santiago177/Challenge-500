from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxValueAfter = [0] * len(prices)
        maxValue = 0
        maxAfter = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            maxValueAfter[i] = maxAfter
            maxAfter = max(maxAfter, prices[i])
        for i in range(len(prices)):
            maxValue = max(maxValue, maxValueAfter[i] - prices[i])

        return maxValue

test = Solution()
print(test.maxProfit([7,1,5,3,6,4]))
print(test.maxProfit([7,6,4,3,1]))
print(test.maxProfit([1]))
print(test.maxProfit([1,8,4,3,6]))