from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1

        for key, value in count.items():
            if value == 1:
                return key

        return 0

    def singleNumber3(self, nums: List[int]) -> int:
        answer = 0
        for i in nums:
            answer ^= i
        return answer



test = Solution()
print(test.singleNumber3([2, 2, 1]))
print(test.singleNumber3([1]))
print(test.singleNumber3([3, 1, 2, 1, 2]))