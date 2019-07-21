#include<vector>
using namespace std;
// 有效数独判断
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<int>rows={0,0,0,0,0,0,0,0,0};
        vector<int>cols={0,0,0,0,0,0,0,0,0};
        vector<int>boxes={0,0,0,0,0,0,0,0,0};
        int cur, index;
        for (int i=0;i<board.size();i++)
            for (int j=0;j<board[i].size();j++) {
                 if (board[i][j] == '.') 
                     continue;
                cur = 1 << (board[i][j] - '1');
                index = i/3*3+j/3;
                if ((rows[i] & cur) != 0 || (cols[j] & cur) != 0 || (boxes[index] & cur) !=0 ) {
                   
                    return false;
                }   
                rows[i] |= cur;
                cols[j] |= cur;
                boxes[index] |= cur;
            }
        return true;
    }       
};