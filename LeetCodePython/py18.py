# 四数之和
class Solution:
    # 固定两个值，左右指针+剪枝
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = list()
        for i in range(n-3):
            # 防止重复 数组进入 result
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 当数组最小值和都大于target 跳出
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # 当数组最大值和都小于target,说明i这个数还是太小,遍历下一个
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            for j in range(i+1, n-2):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = n - 1
                while left<right:
                    cur = nums[i]+nums[j]+nums[left]+nums[right]
                    if cur==target:
                        result.append([nums[i],nums[j],nums[left], nums[right]])
                    if cur<target:
                        left+=1
                        while left<right and nums[left] == nums[left-1]:
                            left+=1
                    else:
                        right-=1
                        while left<right and nums[right] == nums[right+1]:
                            right-=1

        return result
                    
                
            
        