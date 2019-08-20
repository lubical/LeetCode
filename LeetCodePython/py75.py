# 颜色分类0、1、2
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        index = 0
        left = 0
        right = len(nums) - 1
        if right<1:
            return
        
        while index <=right:
            while nums[index] != 1 and index>=left and index<=right:
                if nums[index] == 0:
                    nums[index], nums[left] = nums[left], nums[index]
                    left += 1
                elif nums[index] == 2:
                    nums[index], nums[right] = nums[right], nums[index]
                    right -= 1
                else:
                    return
                # print(index, left, right, nums)
            index = index+1 

class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        '''
        荷兰三色旗问题解
        '''
        # 对于所有 idx < p0 : nums[idx < p0] = 0
        # curr是当前考虑元素的下标
        p0 = curr = 0
        # 对于所有 idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/two-sum/solution/yan-se-fen-lei-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。