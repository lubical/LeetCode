// 不同路径：动态规划
#include <vector>
using namespace std;
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> result(2,vector<int>(n));
        result[0][0] = 1;
        result[1][0] = 1;
        for(int i=0;i<m;i++)
            for(int j=1;j<n;j++)
                result[(i+1)%2][j] = result[i%2][j] + result[(i+1)%2][j-1];
        
        return result[m%2][n-1];
        
    }
};