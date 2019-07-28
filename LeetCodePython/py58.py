# 最后一个单词的长度
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        i = len(s) - 1
        while i>=0 and s[i] == ' ':
            i -= 1
        if i == -1:
            return 0
        ans = ''
        while i>=0 and s[i] != ' ':
            ans = s[i] + ans
            i -= 1
        return len(ans)