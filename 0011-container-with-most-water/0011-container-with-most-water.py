class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        left = 0
        right = len(height) - 1
    
        while left < right:
            h = min(height[left], height[right])
            m = max(m, h * (right - left))
        
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
    
        return m
