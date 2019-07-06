# 最长公共前缀。
# 法一：纵向比较，每一个子串的位置对比
from typing import List, Tuple, Dict
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        ans = ''
        while strs:
            x = strs[0][index] if index<len(strs[0]) else '' 
            for text in strs:
                if index >= len(text) or text[index] != x:
                    return ans
            ans += x
            index += 1
        return ''

# 法二：两个两个对比，当前的最长相似与下一个取最长相似。
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = strs[0]
        for text in strs:
            i = 0
            while i < min(len(text),len(ans)) and ans[i] == text[i]:
                i += 1
            if i == 0:
                return ""
            else:
                ans = text[0:i]
        return ans