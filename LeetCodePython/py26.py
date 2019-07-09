# 删除排序数组中的重复项
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        result = 0
        while index<len(nums):
            if index == 0  or nums[index] != nums[index-1]:
                nums[result] = nums[index]
                result += 1
            index += 1
        return result
        