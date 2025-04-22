from typing import List
class Solution:
    def trap1(self, height: List[int]) -> int:
        maxl, maxr = [0] * len(height), [0] * len(height)
        value = 0
        for i in range(len(height)):
            maxl[i] = value
            value = max(value, height[i])
        value = 0
        for i in range(len(height) - 1, -1, -1):
            maxr[i] = value
            value = max(value, height[i])

        maxWater = 0
        water = 0
        for i, h in enumerate(height):
            if maxl[i] > h and maxr[i] > h:
                water += min(maxl[i], maxr[i]) - h
            maxWater = max(maxWater, water)
        return maxWater

    def trap2(self, height: List[int]) -> int:
        if not height: return 0
        water = 0
        l, r, maxl, maxr = 0, len(height) - 1, 0, 0
        while l < r:
            minh = min(maxl, maxr)
            if maxl <= maxr:
                maxl = max(maxl, height[l])
                if minh > height[l]:
                    water += minh - height[l]
                l += 1
            else:
                maxr = max(maxr, height[r])
                if minh > height[r]:
                    water += minh - height[r]
                r -= 1
        return water

test = Solution()
print(test.trap2([0,1,0,2,1,0,1,3,2,1,2,1]))
print(test.trap2([4,2,0,3,2,5]))
