// x的平方根
class Solution {
public:
    int mySqrt(int x) {
        int left = 0, right = x;
        while (left<right) {
            long mid = (left+right+1L)>>1;
            if (mid*mid>x)
                right = mid -1;
            else
                left = mid;
        }
            
        return left;
    }
};