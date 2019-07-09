
class Solution:
    # 有效符号，栈匹配
    def isValid(self, s: str) -> bool:
        ans = ['#',]
        s = s + '#'
        for i in range(len(s)):
            if ans[-1] == '#' and s[i] == '#' or \
               ans[-1] == '(' and s[i] == ')' or \
               ans[-1] == '{' and s[i] == '}' or \
               ans[-1] == '[' and s[i] == ']':
                ans.pop()
            else:
                ans.append(s[i])
        return not ans

class Solution2:
    def isValid(self, s: str) -> bool:
        lookup = {'{': '}',  '[': ']', '(': ')'}
        stack = []
        for c in s:
            if c in lookup:
                stack.append(c)
                continue
            if stack and lookup[stack[-1]]==c:
                stack.pop()
            else:
                return False
        return not stack
    


                    
        