# 跳跃游戏，能否到达最后
class Solution:
    def canJump(self, nums: List[int]) -> bool:
       # 一次循环能走过最远的
        n = len(nums)
        if n<=1:
            return True
        further = 0
        for index, num in enumerate(nums):
            if index <= further and index + num > further:  # 该步可达，且在该步的基础上能到达更远，则更新可达的距离
                further = index + num
            if further >= n-1: #可达最远点已经可以到最后一个位置，则返回True
                return True
            if index > further:  # 如果该步已经不可达且还没退出，说明已经到不了了 
                return False
        return False