# 通配符匹配
# ？匹配任意一个字符； * 匹配任意字符串，包含空串
# 动态规划
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        
        dp = [[False]*(p_len+1) for _ in range(s_len+1)]
        dp[0][0] = True
        
        for i in range(p_len):
            if p[i]=='*' and dp[0][i]:
                dp[0][i+1] = True
        #print(dp)
        for i in range(s_len):
            for j in range(p_len):
                first_match = p[j] in [s[i], '?']
                if p[j] == '*':
                    dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j]
                else:
                    dp[i+1][j+1] = first_match and dp[i][j]
        #print(dp)
        return dp[-1][-1]