// 通配符匹配
#include <string>
using namespace std;
class Solution {
public:
    bool isMatch(string s, string p) {
        int n = s.size(), m = p.size();
        bool dp[n+1][m+1];
        memset(dp, 0, sizeof(dp));  
        dp[n][m] = true;
        // 循环从n开始，为了处理串s为空时，串p能否匹配的问题
        for (int i=n;i>=0;i--)
            for (int j=m;j>=0;j--) {
                if (i==n && j==m)
                    continue;
                bool first_match = j<m && i<n &&(p[j] =='?' || p[j] == s[i] || p[j] == '*');
                if (j<m && p[j] == '*')
                    //将 * 跳过 和将字符匹配一个并且 pattern 不变两种情况; first_match做了边界处理
                    dp[i][j] = dp[i][j+1] || first_match && dp[i+1][j];
                else
                    dp[i][j] = first_match && dp[i+1][j+1];
            }
                
        return dp[0][0];
        
    }
};