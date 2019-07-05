# 盛最多水的容器
class Solution:
    def maxArea(self, height: List[int]) -> int: 
        left = 0; right = len(height)-1
        ans = (right-left)*min(height[left], height[right])
        while  left<right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            hold = (right-left)*min(height[left], height[right])
            ans = max(ans, hold)
            
        return ans