#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#
# https://leetcode.cn/problems/count-of-range-sum/description/
#
# algorithms
# Hard (41.46%)
# Likes:    447
# Dislikes: 0
# Total Accepted:    30.9K
# Total Submissions: 74.5K
# Testcase Example:  '[-2,5,-1]\n-2\n2'
#
# 给你一个整数数组 nums 以及两个整数 lower 和 upper 。求数组中，值位于范围 [lower, upper] （包含 lower 和
# upper）之内的 区间和的个数 。
# 
# 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-2,5,-1], lower = -2, upper = 2
# 输出：3
# 解释：存在三个区间：[0,0]、[2,2] 和 [0,2] ，对应的区间和分别是：-2 、-1 、2 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0], lower = 0, upper = 0
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -2^31 
# -10^5 
# 题目数据保证答案是一个 32 位 的整数
# 
# 
#

# @lc code=start
class BIT:
    def __init__(self, n) -> None:
        self.n = n
        self.tree = [0] * (n+1)
    
    def lowbit(self, x):
        return x & -x 
    
    def update(self, index, val):
        while index <= self.n:
            self.tree[index] += val 
            index += self.lowbit(index)

    def query(self, index):
        s = 0
        while index:
            s += self.tree[index]
            index -= self.lowbit(index)
        return s

    
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        preSum = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            preSum[i+1] = preSum[i] + num 
        allNumbers = set()
        for num in preSum:
            allNumbers.add(num)
            allNumbers.add(num-lower)
            allNumbers.add(num-upper)
        values = dict()
        idx = 0
        for num in sorted(list(allNumbers)):
            values[num] = idx
            idx += 1
        bit = BIT(len(values))
        res = 0
        for pre in preSum:
            left, right = values[pre - upper], values[pre - lower]
            res += bit.query(right+1) - bit.query(left)
            bit.update(values[pre]+1, 1)
        return res 

# @lc code=end