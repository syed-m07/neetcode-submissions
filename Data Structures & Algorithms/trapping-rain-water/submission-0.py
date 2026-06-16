class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxl = 0
        maxr = 0
        water = 0

        while left < right:
            if maxl < maxr:
                if height[left] < maxl:
                    water += maxl - height[left]
                else:
                    maxl = height[left]
                left += 1
            else:
                if height[right] < maxr:
                    water += maxr - height[right]
                else:
                    maxr = height[right]
                right -= 1
        if height[left] < min(maxl, maxr):
            water += min(maxl, maxr) - height[left]
        return water