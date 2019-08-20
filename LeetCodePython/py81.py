# 搜索旋转链表, 因为可以包含相同数值，因此没办法确定哪一部分有序，因此在前面增加一种判断，nums[mid] == nums[left] == nums[right]
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            #print(left, right)
            mid = left + (right - left) // 2
            # 等于目标值
            if nums[mid] == target:return True
            
            if nums[mid] == nums[left] == nums[right]:
                left += 1
                right -= 1
            # 在前部分
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/two-sum/solution/er-fen-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。