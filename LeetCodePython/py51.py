# N皇后问题
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [False] * n
        lefts = [False] * (2*n+1)
        rights = [False] * (2*n+1)
        tmp = []
        result = []
        def backtrack(row):
            if row == n:
                result.append(tmp[:])
            else:
                for col in range(n):
                    if not cols[col] and not lefts[row+col] and not rights[n+col-row]:
                        cols[col]=lefts[row+col]=rights[n+col-row] = True
                        tmp.append("." * col + "Q" + "." * (n-col-1))
                        backtrack(row+1)
                        tmp.pop()
                        cols[col]=lefts[row+col]=rights[n+col-row] = False
        
        backtrack(0)
        return result