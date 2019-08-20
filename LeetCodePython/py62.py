# 不同路径数
# 动态规划
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = [[0]*n for _ in range(2)]
        result[0][0] = 1
        result[1][0] = 1
        for i in range(m):
            for j in range(1,n):
                result[(i+1)%2][j] = result[i%2][j] + result[(i+1)%2][j-1];
        return result[m%2][n-1]