#include <vector>
#include <string>
using namespace std;
// 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
// 搜索，剪枝判断，左括号用的比右括号少（即剩下的左括号比剩下的右括号多），左右括号有一者为空，为匹配完。
class Solution {
public:
    void helper(int left, int right, string tmp, vector<string> &result) {
        if (left == 0 && right == 0) {
            result.push_back(tmp);
            return;
        }
        
        if (left>right || left<0 || right<0)  //左括号用的比右括号少
            return ;
      
        
        helper(left-1, right, tmp+'(', result);
        helper(left, right-1, tmp+')', result);
        
    }
    vector<string> generateParenthesis(int n) {
        vector<string>result;
        helper(n,n, "", result);
        return result;
    }
};