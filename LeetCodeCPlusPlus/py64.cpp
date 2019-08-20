/*
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
解法：动态规划
 */
#include <vector>
using namespace std;
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        if (grid.empty())
            return 0;
        int n = grid.size(), m = grid[0].size();
        
        for (int i=1;i<m;i++)  // 处理边界第一行
            grid[0][i] += grid[0][i-1];
         
        for (int i=1;i<n;i++)  // 处理边界第一列
            grid[i][0] += grid[i-1][0];
        
        for (int i=1;i<n;i++)
            for (int j=1;j<m;j++)
                grid[i][j] += grid[i-1][j] < grid[i][j-1] ? grid[i-1][j] : grid[i][j-1];
        
        return grid[n-1][m-1];
        
    }
};