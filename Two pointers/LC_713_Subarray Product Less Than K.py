from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        l = 0
        prod = 1
        for r in range(len(nums)):
            prod *= nums[r]
            while l <= r and prod >= k:
                prod = prod // nums[l]
                l += 1
            count += (r - l + 1)
        return count

test = Solution()
print(test.numSubarrayProductLessThanK([10,5,2,6], 100))