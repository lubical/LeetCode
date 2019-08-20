# 删除数组中的重复项，重复次数不超过2次
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        index = 1
        counts = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                counts += 1
            else:
                counts = 1
            if counts <= 2:
                nums[index] = nums[i]
                index += 1
        return index


class Solution2:
    def removeDuplicates(self, nums, k):
        i = 0
        for num in nums:
            if i < k or num != nums[i-k]:
                nums[i] = num
                i += 1
        return i

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/two-sum/solution/shan-chu-pai-xu-shu-zu-zhong-de-zhong-fu-xiang-i-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。