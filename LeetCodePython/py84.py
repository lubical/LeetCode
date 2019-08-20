from typing import List 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调队列，以i为最低柱子的面积最大值，找两端比heights[i]小的第一个值left_i, right_i
        # 面积为 (right_i - left_i - 1 ) * heights[i]
        stack = []
        heights = [0] + heights + [0]
        result = 0
        for i, num in enumerate(heights):
            while stack and heights[stack[-1]] > num:
                top = stack.pop()
                result = max(result, (i-stack[-1]-1) * heights[top])
            stack.append(i)
        return result