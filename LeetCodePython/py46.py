class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tmp = []
        n = len(nums)
        result = []
        used = {}
        def helper(count):
            if count == n:
                result.append(tmp[:])
            else:
                for i in range(n):
                    if i not in used:
                        tmp.append(nums[i])
                        used[i] = 1
                        helper(count+1)
                        tmp.pop()
                        del used[i]
        helper(0)
        return result