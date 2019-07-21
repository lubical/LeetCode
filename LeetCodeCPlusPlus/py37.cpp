// 解数独， 回溯
#include<vector>
#include<bitset>
using namespace std;
class Solution {
private: 
    int boxesIndex(int row, int col) {
        return row / n * n + col / n;
    }

    bool couldPlace(int d, int row, int col) {
        return !(rows[row][d] == 1 || cols[col][d] == 1 || boxes[boxesIndex(row,col)][d] == 1);
    } 
    
    void placeNumber(int d, int row, int col) {
        rows[row][d] = cols[col][d] = boxes[boxesIndex(row, col)][d] = 1;
        (*board)[row][col] = d + '0';
    }
    void removeNumber(int d, int row, int col) {
        rows[row][d] = cols[col][d] = boxes[boxesIndex(row, col)][d] = 0;
        (*board)[row][col] = '.';
    }
    void placeNextNumbers(int row, int col) {
        if (row == N - 1 && col == N - 1) {
            sudokuSolved = true;
        } else {
            if (col == N - 1)
                backTrack(row + 1, 0);
            else
                backTrack(row, col + 1);
        }
    }
    void backTrack(int row, int col) {
        if ((*board)[row][col] == '.') {
            for(int i=1;i<10;i++) {
                if (couldPlace(i, row, col)) {
                    placeNumber(i, row, col);
                    placeNextNumbers(row, col);
                    if (!sudokuSolved)  // 找到就不用回溯了
                        removeNumber(i, row, col);
                        
                }
            }
        } else
            placeNextNumbers(row, col);
    }
public:
    vector<vector<char> > *board;
    vector<bitset<9> > rows;    //行
    vector<bitset<9> > cols;    //列
    vector<bitset<9> > boxes;  // box
    int n = 3;
    int N = n * n;
    bool sudokuSolved = false;
    void solveSudoku(vector<vector<char>>& board) {
        rows.resize(9);
        cols.resize(9);
        boxes.resize(9); // 数组vector空间申请, 否则出现reference binding to null pointer of type
        // for (int i=0;i<N;i++) {
        //     rows[i] = 0;
        //     cols[i] = 0;
        //     boxes[i] = 0;
        // }
        this->board = &board;
        for(int i=0;i<N; i++)
            for (int j=0;j<N;j++)
                if (board[i][j] != '.') {
                    int d = board[i][j] - '0';
                    placeNumber(d, i, j);
                }
        backTrack(0,0);
    }
};