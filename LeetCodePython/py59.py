# 螺旋矩阵 II
# 填充1~n*b到按顺时针顺序螺旋排列正方形矩阵
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left = 0
        right = n-1
        up = 0
        down = n-1
        result = [[0]*n for _ in range(n)]
        num = 1
        while True:
            for i in range(left, right+1):  # 往右走
                result[up][i] = num
                num += 1
            up += 1
            
            if up > down:  
                break
            for i in range(up, down+1):  # 往下走
                result[i][right] = num
                num += 1
            
            right -= 1
            if right<left:
                break
            
            for i in range(right, left-1, -1): # 往左走
                result[down][i] = num
                num += 1
            
            down -= 1
            if down < up:
                break
      
            for i in range(down, up-1, -1): # 往上走
                result[i][left] = num
                num += 1
      
            left += 1
            if left>right:
                break
        return result