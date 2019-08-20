# 最小覆盖子串；滑动窗口，先从左往后找到符合的串，再缩减左窗口直到不满足，再扩展右窗口。。。
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        window = Counter()
        needs = Counter(t)
        ans = float("inf")
        left = right = match = 0
        start = 0
        while right<len(s):
            c1 = s[right]
            if needs[c1] > 0:
                window[c1] += 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1
            while match == len(needs):
                if right - left  < ans:
                    ans = right - left
                    start = left
                c2 = s[left]
                if needs[c2]>0:
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
            
                
        return "" if ans == float("inf") else s[start:start+ans]