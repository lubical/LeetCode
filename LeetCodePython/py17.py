from typing import List
class Solution:
    # 电话号码组合 简单深度搜索
    def searchLetter(self, digits: str, cur:str, pos: int, dic: dict, ans: list):
        if pos == len(digits) - 1:
            for ch in dic[digits[pos]]:
                ans.append(cur+ch)
            return
        else:
            for ch in dic[digits[pos]]:
                self.searchLetter(digits, cur+ch, pos+1, dic, ans)
                
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2' : ['a', 'b', 'c'],
               '3' : ['d', 'e', 'f'],
               '4' : ['g', 'h', 'i'],
               '5' : ['j', 'k', 'l'],
               '6' : ['m', 'n', 'o'],
               '7' : ['p', 'q', 'r', 's'],
               '8' : ['t', 'u', 'v'],
               '9' : ['w', 'x', 'y', 'z']
              }
        ans = []
        if digits:
            self.searchLetter(digits, '', 0, dic, ans)
        if not digits:
            return []
        # n = len(digits)
        # ans = []
        # def helper(i,tmp):
        #     if i == n:
        #         ans.append(tmp)
        #         return 
        #     for alp in lookup[digits[i]]:
        #         helper(i+1,tmp+alp)
        # helper(0,"")

        return ans
        
        