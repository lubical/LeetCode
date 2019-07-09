from typing import List
# 给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
# 解法，从左边或者从右边找一个不同的值替代相同的值
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right = len(nums)-1
        left = 0
        while left<=right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left
                
        