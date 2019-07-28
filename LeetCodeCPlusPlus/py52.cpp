// N皇后II，有多少种解
// x & -x 取最后一个1
// x &(x-1) 去掉最后一个1
class Solution {
private:
    int result = 0;
    void backtrack(int n, int row, int cols, int hills, int dales) {
        if (row == n) {
            result++;
            return;
        }
        int free_columns = (~(cols|hills|dales)) & ((1<<n)-1); // 将可用的位置由0变成1
        while (free_columns!=0) {
            int pick = free_columns & (-free_columns); // 取最后一个1
            backtrack(n, row+1, cols|pick, (hills|pick)<<1, (dales|pick)>>1);
            free_columns &= free_columns-1; //去掉最后一个1
        }
        
    }
public:
    int totalNQueens(int n) {
        backtrack(n, 0, 0, 0, 0);
        return result;
    }
};