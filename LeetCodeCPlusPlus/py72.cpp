// 编辑距离
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size();
        int m = word2.size();
        if (n*m==0)
            return n+m;
        vector<vector<int>> dp(n+1, vector<int>(m+1, 0));
        for (int i = 1; i <= n; i++) {
		    dp[i][0] = i;  // 边界，第二个字符串匹配长度为0时所需的次数
	    }
        for (int j = 1; j <= m; j++) {
            dp[0][j] = j; // 边界，第一个字符串匹配长度为0时所需的次数
        }
        
        for (int i=1; i<=n; i++)
            for (int j=1; j<=m; j++) {
                if (word1[i-1] == word2[j-1]) {
                    dp[i][j] = dp[i-1][j-1];
                } else
                    dp[i][j] = min(dp[i-1][j-1], min(dp[i][j-1], dp[i-1][j])) +1;
                // dp[i-1][j-1] 替换 dp[i][j-1] 插入 dp[i-1][j] 删除 针对i而言
            }
        return dp[n][m];
        
    }
};