class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
 
        while left < right:
            if heights[left] > heights[right]:
                area = heights[right] * (right - left)
                right -= 1
            elif heights[right] > heights[left]:
                area = heights[left] * (right - left)
                left += 1
            else:
                area = heights[left] * (right - left)
                right -= 1
            
            max_area = max(area, max_area)
        
        return max_area