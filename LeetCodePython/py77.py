# 1..n的所有k个数的组合
# 解法一回溯；解法二字典序
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        temp = []
        def helper(cur, count):
            if count == k:
                result.append(temp[:])
            else:
                for i in range(cur, n+1):
                    temp.append(i)
                    helper(i+1, count+1)
                    temp.pop()
        helper(1, 0)
        return result

class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # init first combination
        nums = list(range(1, k + 1)) + [n + 1]
        
        output, j = [], 0
        while j < k:
            # add current combination
            output.append(nums[:k])
            # increase first nums[j] by one
            # if nums[j] + 1 != nums[j + 1]
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1
            
        return output

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/two-sum/solution/zu-he-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。