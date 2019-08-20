# 编辑距离 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。插入、删除、替换
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n == 0:
            return m
        if m == 0:
            return n
        dp = [[m+n]*(m+1) for _ in range(n+1)]
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if j == m:
                    dp[i][j] = n-i
                    continue
                if i == n:
                    dp[i][j] = m-j
                    continue
                
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i][j], dp[i+1][j]+1)  # 删除
                    dp[i][j] = min(dp[i][j], dp[i][j+1]+1)  # 新增
                    dp[i][j] = min(dp[i][j], dp[i+1][j+1]+1) # 替换
                # print(dp[i][j], end = " ")
            #print("\n")
        
        # for i in range(n):
        #     for j in range(m):
        #         print(dp[i][j], end = " ")
        #     print("\n")
        
        return dp[0][0]