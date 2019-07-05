// 正则表达式模拟 . 与 *
#include<string>
#include<vector>
using namespace std;
class Solution {
public:
    bool isMatch(string s, string p) {
        if (p == "")
            return s == "";
        
        bool firstMatch = (s!="") && (p[0] == s[0] || p[0]=='.');
        
        if (p.size()>1 and p[1]=='*') 
            return isMatch(s, p.substr(2)) || firstMatch && isMatch(s.substr(1), p);
        else
            return firstMatch && isMatch(s.substr(1), p.substr(1));
        
    }
};

class Solution {
public:
    bool isMatch(string text, string pattern) {
        int len1 = text.size(), len2 = pattern.size();
        vector<vector<bool>>dp(len1 + 1, vector<bool>(len2 + 1, false));
        dp[len1][len2] = true;
        for (int i=len1;i>=0;i--)
            for (int j=len2-1;j>=0;j--) {
                bool first_match = i<len1 && (pattern[j]==text[i]||pattern[j]=='.')? true:false;
                if (j+1<len2 and pattern[j+1]=='*'){
                    dp[i][j] = dp[i][j+2] || first_match && dp[i+1][j];
                } else
                    dp[i][j] = first_match && dp[i+1][j+1];
            }
        return dp[0][0];
    }
};

