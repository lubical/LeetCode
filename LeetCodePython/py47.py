# 全排列，有重复数字，不允许重复

class Solution(object):
    def permuteUnique(self, nums):
        result = []
        set_ = set()
        def backtrack(nums, tmp):
            if not nums:
                ans = ",".join(str(item)for item in tmp)
                if ans not in set_:
                    result.append(tmp)
                    set_.add(ans)
                return 
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return result