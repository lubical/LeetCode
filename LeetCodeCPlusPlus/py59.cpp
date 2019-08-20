// 螺旋矩阵II
#include <vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> result(n, vector<int>(n));
        int left = 0, right = n - 1, up = 0, down = n - 1, num = 1;
        while (true) {
            for (int i=left; i<=right; i++)  //往右
                result[up][i] = num++;
            if (++up>down) break;
            for (int i=up; i<=down; i++) // 往下
                result[i][right] = num++;
            if (--right<left) break;
            for (int i=right; i>=left; i--) // 往左
                result[down][i] = num++;
            if (--down<up) break;
            for (int i=down; i>=up; i--) // 往上走
                result[i][left] = num++;
            if (++left>right) break;
        }
        return result;
    }
};