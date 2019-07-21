# 在排序数组中查找元素的第一个和最后一个位置
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        low = 0; high = len(nums) -1 
        while low<high:
            mid = (low+high) >> 1
            if nums[mid]>=target:
                high = mid
            else:
                low = mid + 1
        if nums[low] != target:
            return [-1,-1]
        #print(low)
        result = [low]
        high = len(nums) -1 
        while low<high:
            mid = (low+high+1) >> 1  # 此处加1是为了4，5取中间值时取5，这样最后一次就能移动high指针
            if nums[mid]<=target:
                low = mid 
            else:
                high = mid - 1
                
        result.append(low)
        return result
                
        