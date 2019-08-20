# 爬楼梯，可以爬一级或两级，n级台阶共有多少种
class Solution:
    def climbStairs(self, n: int) -> int:
        pre = 1
        ppre = 0
        cur = 0
        for i in range(n):
            cur = pre + ppre
            ppre = pre
            pre = cur
        
        return cur