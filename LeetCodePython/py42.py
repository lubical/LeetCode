# 接雨水； 当前能接多少水取决于左右两边最大值得较小值与自身的差值
from typing import List 

# 其他解法：双指针，从外往内，移动小的，各自维持一个最大值
# 其他解法：栈，从左到右，栈递减，遇到比栈顶大的弹出计算； 横条
class Solution:
    def trap(self, height: List[int]) -> int:
        
        tmp = -1
        n = len(height)
        leftMaxHeight = [0]*n  # 表示当前位置前的最大值，不包含当前位置
        for i in range(1,n):
            if height[i-1]>tmp:
                leftMaxHeight[i] = height[i-1]
                tmp = height[i-1]
            else:
                leftMaxHeight[i] = tmp
        result = 0
        tmp = -1
        for i in range(n-2, 0, -1):
            if tmp<height[i+1]:
                tmp = height[i+1]
            result += max(min(tmp, leftMaxHeight[i])-height[i], 0)
        return result

class Solution2:
    # 栈
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        stack = [0]
        left = 1; right = len(height)
        ans = 0
        while left<right:
            while stack and height[stack[-1]]<height[left]:
                top = stack.pop()
                if not stack:
                    break
                distance = left - stack[-1] - 1
                ans += (min(height[left], height[stack[-1]]) - height[top]) * distance
            stack.append(left)       
            left += 1           
        return ans
        
        