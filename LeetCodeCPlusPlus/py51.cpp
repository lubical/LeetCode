// N皇后问题
#include <vector>
#include <sstream>
#include <string>
using namespace std;
// 回溯+剪枝
class Solution {
private:
    vector<bool> cols;
    vector<bool> lefts;
    vector<bool> rights;
    vector<string> tmp;
    string construct(int col, int n) {
        std::stringstream ss;
        for (int i=0;i<col;i++) 
            ss<<'.';
        ss<<'Q';
        for (int i=col+1;i<n;i++)
            ss<<'.';
        return ss.str();
    }
    void backtrack(vector<vector<string>>&result, int row, int n) {
        if (row == n) {
            result.push_back(tmp);
        }else {
            for (int col = 0; col<n; col++)
                if (!cols[col] && !lefts[row+col] && !rights[row-col+n]) {
                    tmp.push_back(construct(col, n));
                    cols[col] = true;
                    lefts[row+col] = true;
                    rights[row-col+n] = true;
                    backtrack(result, row+1, n);
                    tmp.pop_back();
                    cols[col] = false;
                    lefts[row+col] = false;
                    rights[row-col+n] = false;
                    
                }
        }
    }
public:
    vector<vector<string>> solveNQueens(int n) {
        cols.resize(n);
        lefts.resize(2*n+1);
        rights.resize(2*n+1);
        vector<vector<string>> result;
        backtrack(result, 0, n);
        return result;
        
    }
};