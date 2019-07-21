# 有效数独判断
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result_row = [0]*9 # 行
        result_col = [0]*9 # 列
        result_rc = [0]*9  # 九宫格 row//3*3+col//3
        for row, row_list in enumerate(board):
            for col, ch in enumerate(row_list):
                if ch.isnumeric():
                    num = 1 << (int(ch)-1)
                    if result_row[row] & num == 0 and result_col[col] & num == 0 and result_rc[row//3*3+col//3] & num == 0:
                        result_row[row] |= num
                        result_col[col] |= num
                        result_rc[row//3*3+col//3] |= num
                    else:
                        return False
        return True
        