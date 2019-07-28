// 顺时针旋转90度
#include <vector>
using namespace std;
class Solution {
private:
    void swap(int &a, int &b) {
        int tmp = a;
        a = b;
        b = tmp;
    }
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (int i=0;i<(n>>1); i++)
            for (int j=i;j<n-i-1;j++) {
                int next_i = j;
                int next_j = n - i - 1;
                while (next_i != i || next_j != j) {
                    swap(matrix[i][j], matrix[next_i][next_j]);
                    int tmp = next_i;
                    next_i = next_j;
                    next_j = n - tmp - 1;
                }
                swap(matrix[i][j], matrix[next_i][next_j]);
            }
    }
};