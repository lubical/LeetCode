# 加1
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        add_on = 1
        for i in range(n-1, -1, -1):
            digits[i] += add_on
            
            if digits[i]<10:
                add_on = 0
                break
            else:
                digits[i] -= 10
                add_on = 1
           
        if add_on:
            result = [1]
            result.extend(digits)
            return result
        else:
            return digits
                