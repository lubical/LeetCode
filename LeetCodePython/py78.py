# 子集，返回集合的幂集
from typing import List
class Solution:
    # 借用上一题的字典序算法
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        n = len(nums)
        def helper(n, k):
            indexs = list(range(0, k)) + [n]  # 下标作为字典序
            j = 0
            while j < k:  # 要找k个
                # add current combination
                result.append([])  # 先存入下一个空list
                for i in range(k):
                    result[-1].append(nums[indexs[i]])
                # increase first nums[j] by one
                # if nums[j] + 1 != nums[j + 1]
                j = 0
                while j < k and indexs[j + 1] == indexs[j] + 1:
                    indexs[j] = j
                    j += 1
                indexs[j] += 1
        
       
        # print(result)
        for i in range(1,n+1):
            helper(n, i)
        return result

class Solution2:
    # 迭代法
    def subsets(self, nums: List[int]) -> List[List[int]]:
        dp = [[]]
        for i in range(len(nums)):
            dp = dp + [item+[nums[i]] for item in dp]
            
        return dp 
