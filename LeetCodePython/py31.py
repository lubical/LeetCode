# 下一个字典序列。 从后往前，找到第一个前面的数比后面的数小的位置，再从后面找到比他大的最小值，替换后，将剩余部分排序
from typing import List
class Solution:
    def quicksort(self, nums: List[int], left: int, right: int) -> None:
        if left>=right:
            return
        i, j = left+1, right
        pivot = nums[left]
        while i<=j:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] >= pivot:
                j -= 1
            if i<j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]
        self.quicksort(nums, left, j-1)
        self.quicksort(nums, j+1, right)
        
        
    def nextPermutation(self, nums: List[int]) -> None:
        right = len(nums) - 1
        while right>0 and nums[right-1] >= nums[right]:
            right -= 1
        
        if right>0 and nums[right-1] < nums[right]:  # 能交换的
            index = right
            for i in range(right, len(nums)):    # 往右找个比当前大的最小值交换
                if nums[i] < nums[index] and nums[i] > nums[right-1]:
                    index = i
                    
            nums[right-1], nums[index] = nums[index], nums[right -1]
            self.quicksort(nums, right, len(nums) -1)
            return
        
        
        left = 0; right = len(nums) - 1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

class Solution2:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        实际上因为找的过程中是nums[i]>num[i-1],意味着后面全是 nums[j]<=nums[j-1],即逆序的
        此后找到比nums[i]大的最小值，交换后还是保持着字典序，因此，直接逆序即可。
        """
        def reverse(nums: List[int], left: int, right: int):
            while left<right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        
        n = len(nums) - 1
        index = n
        while index>0 and nums[index] <= nums[index-1]:
            index -= 1
        
        if index > 0:
            for j in range(n, index-1, -1):
                if nums[j] > nums[index-1]:
                    nums[index-1], nums[j] = nums[j], nums[index-1]
                    break
            reverse(nums, index, n)
        else:
            reverse(nums, 0, n)