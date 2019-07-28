# 最大子序和
# 动态规划；大于0继续加，小于0重新开始
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -2147483648
        total = 0
        for num in nums:
            total += num
            result = total if total>result else result
            total = 0 if total<0 else total
        return result