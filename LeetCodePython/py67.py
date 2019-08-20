# 二进制求和
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while (i>=0 or j>=0):
            temp = carry
            temp += int(a[i]) if i>=0 else 0
            temp += int(b[j]) if j>=0 else 0
            result = str(temp%2) + result
            carry = temp // 2
            i -= 1
            j -= 1
        
        if carry:
            result = '1' + result
        
        return result