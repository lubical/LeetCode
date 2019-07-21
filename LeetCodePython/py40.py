# 组合总数II， 数字不可重复，使数字和为给定值
# 回溯
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        filter_set = set()
        tmp = []
        tmp_str = []
        def helper(pos, target):
            if target == 0:
                tmp_str = [str(item) for item in tmp]
                st = ",".join(tmp_str)
                if not st in filter_set:
                    result.append(list(tmp))
                    filter_set.add(st)
            elif pos>=n or candidates[pos]>target:
                return
            else:
                helper(pos+1, target)
                tmp.append(candidates[pos])
                helper(pos+1, target-candidates[pos])
                tmp.pop()
        candidates.sort()
        helper(0, target)
        return result
            