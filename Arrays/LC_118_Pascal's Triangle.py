from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row = [1]
        allRows = []
        for i in range(numRows):
            allRows.append(row)
            if i == 0:
                row = [1, 1]
            else:
                copy = row.copy()
                row = [1]
                for j in range(len(copy) - 1):
                    row.append(copy[j] + copy[j + 1])
                row.append(1)

        return allRows

test = Solution()
print(test.generate(1))
print(test.generate(5))
print(test.generate(30))