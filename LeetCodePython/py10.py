# 实现正则表达式.与*的功能
class Solution:          
    # 搜索 关于*两个字符一起判断会省事很多，自顶向下
    def isMatch(self, text: str, pattern: str) -> bool:
        if not pattern:  # 如果匹配字符为空
            return not text  # 原字符是否为空 
        
        first_match = bool(text) and pattern[0] in {text[0],'.'}  
        # 当前字符与匹配串第一个字符能否匹配，前提text不为空，pattern为空已经在上面返回了 {a ,b}是set
        
        if len(pattern)>1 and pattern[1] == '*':  
            # 长度为2，且第二个字符为*才有匹配*的用处, 关于a*的匹配方式是把所有的a匹配完了，再用去掉a的方式，即跳过a*
            return (self.isMatch(text, pattern[2:]) or first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

class Solution:          
    # 搜索 自顶向下,增加备忘录
    def isMatch(self, text: str, pattern: str) -> bool:
        memo = {}
        
        def dp(i,j):
            if (i,j)  not in memo: 
                if j==len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i<len(text) and pattern[j] in {text[i],'.'}  # 当前字符与匹配串第一个字符能否匹配，前提text不为空，pattern为空已经在上面返回了

                    if j+1<len(pattern) and pattern[j+1] == '*':  # 长度为2，且第二个字符为*才有匹配*的用处, 关于a*的匹配方式是把所有的a匹配完了，再用去掉a的方式，即跳过a*
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)
                memo[i,j] = ans
            return memo[i,j]
        return dp(0,0)
        

class Solution:          
    # 搜索 关于*两个字符一起判断会省事很多，自底向上
    def isMatch(self, text: str, pattern: str) -> bool:
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        
        dp[-1][-1] = True
        for i in range(len(text), -1 , -1):  # 此处从len(text)开始新增了一个字符，是为了匹配 源串a="", 匹配串b=x*。由于源串的长度大于等于匹配串，因此只需新增一列即可。
            for j in range(len(pattern)-1, -1, -1):
                first_match = i < len(text) and  pattern[j] in {text[i], '.'}
                if j+1<len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        
#         for i in range(len(text)+1):
#             for j in range(len(pattern)+1):
#                 print(dp[i][j], end=" ")
#             print("\n")
        return dp[0][0]
        
        
        