# x的平方根
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left<right:
            mid = (left+right+1)>>1
            if mid*mid>x:
                right = mid -1
            else:
                left = mid
        return left

class Solution2:
    # 牛顿法 一阶泰勒公式 fx = fx0 + (x-x0)*f'(x0)
    # 不断逼近
    def mySqrt(self, x):
        if x < 0:
            raise Exception('不能输入负数')
        if x == 0:
            return 0
        # 起始的时候在 1 ，这可以比较随意设置， 设置负数有可能得到负数的平方根
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)

# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/two-sum/solution/er-fen-cha-zhao-niu-dun-fa-python-dai-ma-by-liweiw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。