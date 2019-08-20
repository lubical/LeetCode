// 搜索二维矩阵
// # 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
// # 每行中的整数从左到右按升序排列。
// # 每行的第一个整数大于前一行的最后一个整数。
// 解法 二分
#include <vector>
using namespace std;
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n = matrix.size();
        if (n==0)
            return false;
        int m = matrix[0].size();
        int left=0, right = n*m-1;
        while (left<=right) {
            int mid = (left+right) >> 1;
            int key = matrix[mid / m][mid % m];
            if (key == target)
                return true;
            if (key < target)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return false;
    }
};
