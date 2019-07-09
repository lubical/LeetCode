#include <iostream>
using namespace std;
// 两数相除，求商，不用乘除模
class Solution {
public:
    int divide(int dividend, int divisor) {
        int sign = (dividend > 0) ^ (divisor > 0);
        int count = 0;
        long result = 0;
        long dividend_t = abs((long)dividend);
        long divisor_t = abs((long)divisor);

        while (dividend_t>=divisor_t) {
            count++;
            divisor_t <<= 1;
        }
        while (count>0) {
            count--;
            divisor_t >>= 1;
            if (dividend_t >= divisor_t) {
                result += 1L << count;    // 此处注意要写1L，表明以long int作为移位对象，否则默认为int
                dividend_t -= divisor_t;
            }
        }
        
        result = sign? -result : result;
        
        if (result>=INT_MIN && result<= INT_MAX)
            return result;
        else
            return INT_MAX;


    }
};