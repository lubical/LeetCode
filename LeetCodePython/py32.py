# 最长的有效()对的长度
# 动态规划、栈、暴力、左到右，右到左各一遍判断括号数。
class Solution:
    # 动态规划
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0]*n
        result = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(': # 最简单的状态转移
                    dp[i] = dp[i-2] + 2
                elif i-dp[i-1]-1 >=0 and s[i-dp[i-1]-1] == '(': 
                    # )),考虑i-dp[i-1]-1 是否能和当前的')'匹配，若能，则补上之前的与dp[i-1]+2
                        dp[i] = dp[i-1] + 2 + dp[max(0,i-dp[i-1]-2)]
                result = max(result, dp[i])
                    
        return result 


class Solution2:
    # 栈的思路，加入一个额外的标志位，当有一个括号匹配时，弹出栈后，当前栈顶的元素位置与当前位置的差值就是匹配长度
    def longestValidParentheses(self, s: str) -> int:
        left = 0; right = len(s)
        result = 0
        stack = [-1]
        while left<right:
            if s[left]=='(':
                stack.append(left)
            else:
                if len(stack)>1:  #  有两个以上左括号
                    stack.pop()
                    result = max(result, left-stack[-1])
                else: # 只有一个标志位
                    stack.pop()
                    stack.append(left)  # 加入新的标志位
                    
            left += 1      
                    
            
                
        return result 