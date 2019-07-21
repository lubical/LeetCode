# 缺失的最小正数
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 如果按顺序存放，扫描一遍就可以了
        # 不按顺序且数字连续，可以把数字放到相应的位置-1（数组从0开始）
        # 从左到右，判断当前的数字，大于数组长度或者是负数直接丢弃置为-1；否则将相应位置的数字交换过来，再判断
        for i in range(len(nums)):
            while nums[i]!=i+1 and nums[i]>0 and nums[i] <= len(nums) and nums[nums[i]-1]!=nums[i]:
                # 当前位置不对；且当前数字小于数组长度；且对应正确位置上的值不在正确位置
                d = nums[i]-1
                nums[i], nums[d] = nums[d], nums[i]
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1