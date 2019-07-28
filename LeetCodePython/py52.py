# N皇后II，有多少种解法
class Solution:
    def totalNQueens(self, n: int) -> int:
        # x & -x 代表除最后一位 1 保留，其它位全部为 0
        # x & (x - 1) 代表将最后一位 1 变成 0
        
        def backtrack(row, cols, hills, dales):
            if row == n:
                nonlocal result
                result += 1
                return
            free_columns = ~(cols|hills|dales) & ((1<<n)-1)
           
            while free_columns:
                pick = free_columns & (-free_columns) # 取最后一个1
                backtrack(row+1, cols|pick, (hills|pick)<<1, (dales|pick)>>1)
                free_columns =free_columns & (free_columns - 1)
        
        result = 0
        backtrack(0,0,0,0)
        return result