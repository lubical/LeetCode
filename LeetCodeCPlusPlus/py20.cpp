#include <map>
#include <stack>
#include <string>
using namespace std;
// 括号匹配，栈问题
class Solution {
public:
    bool isValid(string s) {
        map<char,char> lookup = {
                {'[', ']'},
                {'{', '}'},
                {'(', ')'}
        };
        stack<char> mystack;
        for(auto i:s) {
            if (lookup.count(i)==1){
                mystack.push(i);
                continue;
            } 
            else if(!mystack.empty() && lookup[mystack.top()] == i) 
                mystack.pop();
            else
                return false;
        }
    return mystack.empty();
   }
};
