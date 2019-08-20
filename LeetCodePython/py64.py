"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
解法：动态规划
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        
        for j in range(1,m):  # 预处理第一行
            grid[0][j] += grid[0][j-1]
            
        for i in range(1,n):
            for j in range(m):
                if j == 0:    # 处理边界第一列
                    grid[i][j] += grid[i-1][j]
                    continue
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
#         for i in range(n):
#             for j in range(m):
#                 print(grid[i][j], end=" ")
#             print("\n")
        
        return grid[n-1][m-1]