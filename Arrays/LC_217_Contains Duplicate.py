from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checkSet = set()
        for i in nums:
            checkSet.add(i)

        return len(checkSet) != len(nums)

test = Solution()
print(test.containsDuplicate([2, 2, 1]))
print(test.containsDuplicate([1]))
print(test.containsDuplicate([3, 1, 2, 1, 2]))
print(test.containsDuplicate([3, 1, 2]))