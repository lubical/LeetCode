def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        low = 0; high = len(nums) -1 
        while low<high:   # 找左端相等值
            mid = (low+high) >> 1 # 4,5 中间值落在左端4
            if nums[mid]>=target:
                high = mid
            else:
                low = mid + 1
        if nums[low] != target:
            return [-1,-1]
        #print(low)
        result = [low]   
        high = len(nums) -1  # 找右端相等值
        while low<high:
            mid = (low+high+1) >> 1  # 此处加1是为了4，5取中间值时取5，这样最后一次就能移动high指针
            if nums[mid]<=target:
                low = mid 
            else:
                high = mid - 1
                
        result.append(low)
        return result

def searchInsert(nums: List[int], target: int) -> int:
        if not nums:
            return 0
        left = 0; right = len(nums) - 1
        while left<=right:
            mid = (left+right)>>1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left