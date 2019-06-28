class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0
        dict = {}
        while right<len(s):
            pos = dict.get(s[right], -1)
            if pos<left:  # 未重复-1；或者重复值在滑动窗口左端边界外 
                dict[s[right]] = right
                ans = max(ans, right-left+1)
                right+=1
            else:
                left = pos+1  # 更新滑动窗口左边界
        return ans

if __name__ == '__main__':
    import time
    start = time.process_time()
    source = "abcabcbb"
    ans = Solution().lengthOfLongestSubstring(source)
    print(ans)
    end = time.process_time()
    print(str(end-start))
