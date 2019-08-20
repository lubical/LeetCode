# 矩阵置0
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n==0:
            return
        m = len(matrix[0])
        row = set()
        col = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        for i in range(n):
            for j in range(m):
                if i in row or j in col:
                    matrix[i][j] = 0
        