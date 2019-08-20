# 不同路径II，带有障碍点,动态规划
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        result = [[0]*n for _ in range(2)]
        result[0][0] = 1
        for i in range(m):
            for j in range(n):
                if j == 0:
                    if not obstacleGrid[i][j]:
                        result[(i+1)%2][j] = result[i%2][j]
                    else:
                        result[(i+1)%2][j] = 0
                    continue
                if not obstacleGrid[i][j]:
                    result[(i+1)%2][j] = result[i%2][j] + result[(i+1)%2][j-1];
                else:
                    result[(i+1)%2][j] = 0
        return result[m%2][n-1]