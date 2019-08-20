// 不同路径II，带有障碍点
#include <vector>
using namespace std;
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if (obstacleGrid.empty())
            return 0;
        int n = obstacleGrid[0].size();
        int m = obstacleGrid.size();
        vector<vector<long>> result(2,vector<long>(n));  // 中间结果超过int
        result[0][0] = 1;
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++) {
                if (j==0) {
                    if (!obstacleGrid[i][j])
                        result[(i+1)%2][j] = result[i%2][j];
                    else
                        result[(i+1)%2][j] = 0;
                    continue;
                }
                if (!obstacleGrid[i][j])
                    result[(i+1)%2][j] = result[i%2][j] + result[(i+1)%2][j-1];
                else
                    result[(i+1)%2][j] = 0;
            }
                
        
        return result[m%2][n-1];
    }
};