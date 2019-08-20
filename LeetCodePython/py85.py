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


class Solution2:
    # 法二，动态规划，每一层，以第i根柱子的高度为最低高度，左右两边所能延伸的最大距离
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n # initialize left as the leftmost boundary possible
        right = [n] * n # initialize right as the rightmost boundary possible
        height = [0] * n

        maxarea = 0

        for i in range(m):

            cur_left, cur_right = 0, n
            # update height
            for j in range(n):
                if matrix[i][j] == '1': height[j] += 1
                else: height[j] = 0
            # update left
            for j in range(n):
                if matrix[i][j] == '1': left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update right
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1': right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update the area
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))

        return maxarea

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/maximal-rectangle/solution/zui-da-ju-xing-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。