from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPointer = 0
        rightPointer = len(height) - 1
        maxArea = 0
        while leftPointer < rightPointer:
            maxArea = max(maxArea, (rightPointer - leftPointer) * min(height[leftPointer], height[rightPointer]))
            if height[leftPointer] < height[rightPointer]:
                leftPointer += 1
            else:
                rightPointer -= 1

        return maxArea

test = Solution()
print(test.maxArea([1,8,6,2,5,4,8,3,7]))
print(test.maxArea([1,8,6,69,5,69,8,3,7]))
print(test.maxArea([1, 1]))