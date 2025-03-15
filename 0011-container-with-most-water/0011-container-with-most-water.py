class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        currentArea = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            if currentArea > maxArea:
                maxArea = currentArea
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
            

        