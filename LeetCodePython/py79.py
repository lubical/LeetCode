# 单词搜索，二维数组中出现给定单词，可上下左右连接，但不能重复使用同一个单元格
# 解法：回溯
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        if n == 0:
            return False
        m = len(board[0])
        
        def backtrack(i, j, k, visited):
            if k == len(word) - 1:
                return board[i][j] == word[k] # 因为每次进来的当前都是没有判断的，所以最后要这样返回
            if board[i][j] == word[k]:
                visited.add((i,j))
                for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    temp_x = i + x
                    temp_y = j + y
                    if 0<=temp_x < n and 0 <= temp_y < m and (temp_x, temp_y) not in visited \
                        and backtrack(temp_x, temp_y, k+1, visited):
                        return True
                visited.remove((i, j))
            return False
        
        for i in range(n):
            for j in range(m):
                if backtrack(i,j, 0, set()):
                    return True
        return False