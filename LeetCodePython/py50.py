# 实现pow(x,y)，及x的幂次方
# 快速幂
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            return self.myPow(1/x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        else:
            half = self.myPow(x, n//2)
            if n%2 ==0:
                return half * half
            else:
                return half * half * x