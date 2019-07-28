//实现 pow(x, n) ，即计算 x 的 n 次幂函数。
// 快速幂
class Solution {
public:
    double myPow(double x, int n) {
        if (n==0)
            return 1.0;
        double tmp = myPow(x, n/2);
        if (n%2==0)
            return tmp*tmp;
        else
            return n<0? 1/x*tmp*tmp : tmp*tmp*x; // 这里不能直接判断n小于0，返回myPow(1/x,-n), n=-2147483648时溢出
    }
};