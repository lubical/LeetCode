// 单词搜索，二维数组中相邻词之间是否出现给定单词
#include <vector>
#include <string>
using namespace std;
class Solution {
    vector<vector<char>>board;
	vector<int>dirx{0,1,0,-1};
	vector<int>diry{1,0,-1,0};
    string word;
    bool backtrack(vector<vector<bool>> &visited, int x, int y, int k) {
        if (k == word.size())
            return true;
        for(int i=0;i<4;i++) {
            int new_x = x + dirx[i];
            int new_y = y + diry[i];
            if (new_x < board.size() && new_x >=0 && new_y < board[0].size() && new_y >=0 
                && board[new_x][new_y] == word[k] && !visited[new_x][new_y]) {
                visited[new_x][new_y] = true;
                if (backtrack(visited, new_x, new_y, k+1))
                    return true;
                visited[new_x][new_y] = false;
            }
        }
        return false;
    }
public:
    bool exist(vector<vector<char>>& board, string word) {
        this->board = board;
        this->word = word;
        vector<vector<bool>> visited(board.size(), vector<bool>(board[0].size(), 0));
        for (int i=0;i<board.size(); i++)
            for (int j=0;j<board[0].size(); j++)
                if (board[i][j] == word[0]) {
                    visited[i][j] =  true;
                    if (backtrack(visited, i,j,1))
                        return true;
                    visited[i][j] =  false;
                }
        return false;
    }
};