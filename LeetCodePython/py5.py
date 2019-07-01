# class Solution:
#     def checkPolindrome(self, s: str) -> bool:
#         i = 0
#         j = len(s)-1
#         while i<j:
#             if s[i]!=s[j]:
#                 return False
#             i+=1
#             j-=1
#         return True
    
#     def longestPalindrome(self, s: str) -> str:
#         if not s:
#             return ''
#         # 二分长度, 直接二分长度不行，因为3个成立，2个有可能不成立
#         # 但是长度为4成立，则2一定成立，长度为5成立，则3一定成立
#         # 因此每次判断两个一奇一偶，不满足才能长度减一。
#         ans = ''
#         l = 0
#         r = len(s)
#         while l<=r:
#             mid = (l+r)//2
#             find = False
       
#             for i in range(len(s)-mid+1):
#                 if self.checkPolindrome(s[i:i+mid]):
#                     find = True
#                     ans = s[i:i+mid]
#                     break
                    
#             for i in range(len(s)-mid):
#                 if self.checkPolindrome(s[i:i+mid+1]):
#                     find = True
#                     ans = s[i:i+mid+1]
#                     break   
#             if find:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return ans
            
class Solution:
    # 中心扩散算法
    def checkPolindrome(self, s: str, i:int, j:int) -> str:
        if j>=len(s) or i<0 or s[i]!=s[j]:
            return ""
        while (i>=0 and j<len(s) and s[i] == s[j]):
            i-=1
            j+=1
        return s[i+1:j]
    
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        
        for i in range(len(s)):
            result = self.checkPolindrome(s,i,i)
            ans = ans if len(ans)>len(result) else result
            result = self.checkPolindrome(s,i,i+1)
            ans = ans if len(ans)>len(result) else result
            
        return ans
            
            
        
            
        