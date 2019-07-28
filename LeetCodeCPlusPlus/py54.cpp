// 螺旋矩阵
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        if (matrix.empty())
            return result;
        int u = 0;
        int l = 0;
        int r = matrix[0].size() - 1;
        int d = matrix.size() - 1;
        while(true) {
            for (int i=l;i<=r;i++) result.push_back(matrix[u][i]); // 往右走
            if (++u > d) break; // 修改上边界
            for (int i=u;i<=d;i++) result.push_back(matrix[i][r]); // 往下走
            if (--r < l) break; // 修改右边界
            for (int i=r;i>=l;i--) result.push_back(matrix[d][i]); // 往左走
            if (--d < u) break; // 修改下边界
            for (int i=d;i>=u;i--) result.push_back(matrix[i][l]); // 往上走
            if (++l > r) break; // 修改左边界
        }
        return result;
    }
};