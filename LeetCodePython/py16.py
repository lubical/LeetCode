from typing import List
class Solution:
    # 三数之和最小，转化为两数和最小。首先计算所有的两数和，并记录组成部分；再遍历结果dict与原来的数组，没出现过的计算值，并更新
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        dic = {}
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] not in dic:
                    dic[nums[i]+nums[j]] = []
                    dic[nums[i]+nums[j]].append(set({i,j}))
                else:
                    dic[nums[i]+nums[j]].append(set({i,j}))
        ans = 2**32 - 1
        result = 0
        for index, num in enumerate(nums):
            for key, value_list in dic.items():
                flag = False
                if ans <= abs(target-key-num):
                    continue
                for value_set in value_list:
                    if index not in value_set:
                        flag = True
                        break
                if flag:
                    ans = abs(target-key-num)
                    result = key+num
        return result

class Solution2:
    # 三数和，固定左端，左右两个指针遍历，判断值
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        n = len(nums) 
        ans = float('inf')
        for index,num in enumerate(nums):
            if index>0 and nums[index] == nums[index-1]:
                continue
            left = index + 1
            right = n - 1
            while left<right:
                cur = nums[index] + nums[left] + nums[right]
                if cur == target:
                    return target
                if abs(cur-target) < abs(ans-target):
                    ans = cur
                if cur < target:
                    left += 1
                else:
                    right -= 1
        return ans   

    def threeSumClosest2(self, nums, target):
            """
            该算法是对双指针的改进版，判断最小的两个数是否大于target，与最大的两个数是否小于target，之后的相同。以下代码来自CSDN用户
            [link](https://blog.csdn.net/TeFuirnever/article/details/94444437)
            @author TeFuirnever
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
            result = list()
            nums.sort()
            for i,m in enumerate(nums[0:-2]):
                l, r = i + 1, len(nums) - 1
                if nums[l] + nums[l + 1] + m > target:
                    result.append(nums[l] + nums[l + 1] + m)
                elif nums[r] + nums[r - 1] + m < target:
                    result.append(nums[r] + nums[r - 1] + m)
                else:
                    while l < r:
                        result.append(nums[l] + nums[r] + m)
                        if nums[l] + nums[r] + m < target:
                            l += 1
                        elif nums[l] + nums[r] + m > target:
                            r -= 1
                        else:
                            return target
            result.sort(key=lambda x:abs(x-target))
            return result[0]
                
        
        