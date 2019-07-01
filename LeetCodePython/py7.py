# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
/*
对于整型数a，b来说，取模运算或者求余运算的方法都是：

求整数商： c = a/b;
计算模或者余数： r = a - c*b
但是求模运算和求余运算在第一步不同，取余运算在取c的值时，向0 方向舍入(fix()函数)，而取模运算在计算c的值时，向负无穷方向舍入(floor()函数)。

作者：cat01
链接：https://leetcode-cn.com/problems/two-sum/solution/pythonqiu-yu-yu-dao-de-keng-by-cat01/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*
*/

class Solution:
    # python的int实际位数超过了32位，因此直接偷懒，算出结果再判断
    def reverse(self, x: int) -> int:
        ans = 0
        flag = 1 if x>0 else -1
        y = abs(x)
        while y>0:
            ans = ans*10+y%10
            y//=10
  
        ans = ans*flag
        if ans>2**31-1 or ans<-2**31:
            return 0
        else:
            return ans

class Solution:
 #   作者：cat01
# 链接：https://leetcode-cn.com/problems/two-sum/solution/pythonqiu-yu-yu-dao-de-keng-by-cat01/
    def reverse(self, x: int) -> int:
        INT_MAX = pow(2,31) - 1
        INT_MIN = - pow(2,31)
        rev = 0
        while x!=0:
            if x > 0:
                pop = x%10
                x = x//10
            else:
                # 针对负数情况进行改造，确保python取模的结果是和取余一致的
                pop = x%-10 # %-10相当于x取正号了
                x = -(x//-10)
            if rev > INT_MAX/10 or (rev== INT_MAX//10 and pop > 7):
                return 0
            if rev < INT_MIN/10 or (rev == INT_MIN//10 and pop < -8):
                return 0
            rev = rev*10 + pop
            
        return rev
        