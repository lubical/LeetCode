// 爬楼梯，可以爬一级或两级，n级台阶共有多少种
class Solution {
public:
    int climbStairs(int n) {
        int ppre = 0;
        int pre = 1;
        int cur = 0;
        for (int i = 0; i<n; i++) {
            cur = ppre + pre;
            ppre = pre;
            pre = cur;
        }
        return cur;
    }
};