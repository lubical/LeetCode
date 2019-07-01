#include<string>
#include<vector>
using namespace std;
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;

        vector<string> rows(min(numRows, int(s.size())));
        int curRow = 0;
        int direction = -1;  //第一轮从0开始，会变方向，因此设置成反方向

        for (char c : s) {
            rows[curRow] += c;
            if (curRow == 0 || curRow == numRows - 1) direction = -direction;
            curRow += direction;
        }

        string ret;
        for (string row : rows) ret += row;
        return ret;
    }
};