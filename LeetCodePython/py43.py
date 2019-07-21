# 数字相乘
from typing import List 
class Solution:
    def multiply_one(self, num: str, i: int, tail: int):
        tmp = []
        if tail:  # 补末尾的0，高位值乘的时候需要
            tmp = [0] * tail
        carry = 0
        n = len(num)
        for index in range(n):
            pre = int(num[n - index - 1])
            now = i * pre + carry
            tmp.append(now % 10)
            carry = now // 10
        if carry:
            tmp.append(carry)
        return tmp

    def sum_num(self, num1: List, num2: List):
        n1 = len(num1)
        n2 = len(num2)
        if n1 < n2:
            return self.sum_num(num2, num1)
        if n2 == 0:
            return num1
        carry = 0
        for i in range(n2):
            tmp = num1[i] + num2[i] + carry
            num1[i] = tmp % 10
            carry = tmp // 10
        i = n2
        while carry:
            if i > n1-1:
                n1 += 1
                num1.append(0)
            tmp = num1[i] + carry
            num1[i] = tmp % 10
            carry = tmp // 10
            i += 1
        return num1

    def multiply(self, num1: str, num2: str) -> str:
        result = []
        n1 = len(num1)
        n2 = len(num2)
        if n1 < n2:
            return self.multiply(num2, num1)
        if num2 == "0" or num1 == "0":
            return "0"
        tail_zeros = 0
        for i in range(n2-1, -1, -1):
            j = int(num2[i])
            tmp = self.multiply_one(num1, j, tail_zeros)
            result = self.sum_num(tmp, result)
            tail_zeros += 1
        result.reverse()
        result = [str(item) for item in result]
        return "".join(result)