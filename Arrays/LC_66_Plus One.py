from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        nine_index = -1

        while True:
            if i == -1:
                digits[i + 1 :nine_index + 1] = [0] * (nine_index - i)
                digits.insert(0, 1)
                break
            if digits[i] != 9:
                digits[i] += 1
                digits[i + 1 :nine_index + 1] = [0] * (nine_index - i)
                break
            else:
                nine_index = max(nine_index, i)
                i -= 1
        return digits


test = Solution()

print(test.plusOne([1, 2]))
print(test.plusOne([9, 9]))
print(test.plusOne([9]))
print(test.plusOne([0]))
print(test.plusOne([8]))
print(test.plusOne([1, 9, 9]))

