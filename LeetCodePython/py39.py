# 组合总数， 和等于target的所有给定数字的组合方式，可重复。
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        candidates.sort()
        def helper(index, total, current):
            if index>=n or total+candidates[index]>target:
                return 
            elif total + candidates[index] == target:
                current.append(candidates[index])
                result.append(list(current))
                current.pop()
                return
            else:
                helper(index+1, total ,current)
                current.append(candidates[index])
                helper(index, total+candidates[index], current)
                current.pop()
        helper(0,0,[])
        return result