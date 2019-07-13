# 搜索旋转排序数组，时间复杂度要求logn
class Solution:
    # 法一，先二分出旋转点，后再根据值大小在相应区间进行二分
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        def binsearch(nums: List[int], left: int, right:int, target:int):
            while left<right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid]>target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        n = len(nums)-1 
        left = 0; right = n
        while left<right:    # 找出旋转点,即第一个小于nums[0]的位置
            mid = (left+right)//2
            if nums[mid]>nums[0]:
                left = mid + 1
            else:
                right = mid  # 为了保证找到的位置是小于nums[0], 此处取mid
                
        if nums[left] == target:
            return left
        if left == 0:  # 已经是有序的，没有旋转点, 或者第一个数是最大的
            left = n+1 if n>=1 and nums[0]<nums[1] else 1
        if target >= nums[0]:
            pos = binsearch(nums, 0, left-1, target)
        else:
            pos = binsearch(nums, left, n, target)
     
        if pos<=n and pos>=0 and nums[pos] == target:
            return pos
        else:
            return -1


class Solution2:
    # 法二，中心点的左右两侧必定有一侧是有序的
    def search(self, nums: List[int], target: int) -> int:
        left = 0; right = len(nums)-1
        while left <= right:
            mid = (left + right) >> 1
            
            if nums[mid] == target:
                return mid
            
            if nums[mid]<nums[right]: # 旋转点在左侧，右侧有序
                if target>nums[mid] and target<=nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target>=nums[left] and target<nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
            