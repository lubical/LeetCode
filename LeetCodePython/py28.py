# 实现 strStr() 函数。
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            find = True
            for j in range(len(needle)):
                if haystack[i+j]!=needle[j]:
                    find = False
                    break
            if find:
                return i
        return -1
        