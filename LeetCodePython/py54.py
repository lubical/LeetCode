# 螺旋矩阵
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if n==0:
            return []
        result = []
        m = len(matrix[0])
        for i in range(min((n+1)>>1, (m+1)>>1)):
            for r in range(i,m-i):  # 右边
                result.append(matrix[i][r])
            if len(result) == n*m:
                break
            for d in range(i+1,n-i):  # 下边
                result.append(matrix[d][m-i-1])
            if len(result) == n*m:
                break
            for l in range(m-i-2, i-1, -1):  # 左边
                result.append(matrix[n-i-1][l])
            if len(result) == n*m:
                break
            for u in range(n-i-2, i, -1): #上边
                result.append(matrix[u][i])
        
        return result
            