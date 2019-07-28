# 顺时针旋转90度 
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        aij  ->  aj(n-i+1)
        aij  <- a(n+1-j)i
         一圈一圈的往内，每一圈的第一个，四份之一的倒金字塔
        """
        n = len(matrix)
        for i in range((n+1)//2):
            for j in range(i, n-i-1):
                next_i, next_j = j, n - i - 1
                # print(i,j, next_i, next_j)
                while (next_i != i or next_j != j):
                    matrix[next_i][next_j],matrix[i][j] = matrix[i][j],matrix[next_i][next_j]
                    #next_j, next_i = n - next_i - 1, next_j
                    next_i, next_j = next_j, n - next_i - 1
                    # tmp = next_j
                    # next_j = n - next_i - 1
                    # next_i = tmp
                    # print(i,j, next_i, next_j)
                matrix[next_i][next_j],matrix[i][j] = matrix[i][j],matrix[next_i][next_j]
                #  print("\n")