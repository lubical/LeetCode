#include <stack>
#include <string>
using namespace std;
// 最长的括号对长度。栈实现。一个标志位。
class Solution {
public:
    int longestValidParentheses(string s) {
        int left = 0, right = s.size();
        stack<int> _stack;
        _stack.push(-1);
        int result = 0;
        while (left<right) {
            if (s[left] == '(')
                _stack.push(left);
            else {
                if (_stack.size() > 1) {
                    _stack.pop();
                    result = max(result, left-_stack.top());
                } else {
                    _stack.pop();
                    _stack.push(left);
                }
            }
            left++;
        }
       return result;
    }
};