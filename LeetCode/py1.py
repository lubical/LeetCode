# 题目描述：给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 思路：暴力枚举，两重循环判断和是否满足条件
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return [0,0]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    ans = Solution().twoSum(nums, target)
    print(ans)


