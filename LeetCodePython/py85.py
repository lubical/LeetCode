#给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
from typing import List
class Solution:
    def leetcode84(self, heights: List[int]) -> int:
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
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        maxarea = 0
        dp = [0]*len(matrix[0]) #以i,j为矩形右下角顶点的最大矩形面积
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
                
            maxarea = max(maxarea, self.leetcode84(dp))
        return maxarea