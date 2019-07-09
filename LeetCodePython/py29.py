# 求两个整数相除的商，要求不能用乘，除，模
class Solution:
    # 解法，模拟除法的过程，位运算实现乘除。
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        result = 0
        while count > 0:
            count -= 1
            divisor >>= 1
            if dividend >= divisor:
                result += 1 << count   # 把 count+1 位上的1转换为10进制
                dividend -= divisor
        result = -result if sign else result
        return result if -(1<<31) <= result <= (1<<31) -1 else (1<<31) -1

class Solution2:
    # 思路二，求除的次数，采用倍增来减少次数，直接上别人代码
    # 作者：powcai
    # 链接：https://leetcode-cn.com/problems/two-sum/solution/liang-shu-xiang-chu-by-powcai/
    def divide(self, divd: int, dior: int) -> int:
        res = 0
        sign =  1 if divd ^ dior >= 0 else -1
        #print(sign)
        divd = abs(divd)
        dior = abs(dior)
        while divd >= dior:
            tmp, i = dior, 1    # 从新开始
            while divd >= tmp:  # 倍增
                divd -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        res = res * sign 
        return min(max(-2**31, res), 2**31-1)


        
        
        