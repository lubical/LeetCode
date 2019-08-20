// 矩阵置0
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        unordered_set<int> row, col;
        int n = matrix.size();
        if (n == 0)
            return;
        int m = matrix[0].size();
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
                if (matrix[i][j] == 0) {
                    row.insert(i);
                    col.insert(j);
                }
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
                if (row.count(i) == 1 || col.count(j) == 1) 
                    matrix[i][j] = 0;
        
    }
};