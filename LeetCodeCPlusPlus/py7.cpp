#include<iostream>
using namespace std;
class Solution {
public:
    // 逆序算出来，判断一下就行了，下面是官方题解。
    int reverse(int x) {
        int rev = 0,pop = 0;
        while(x!=0){
            pop = x % 10;
            x = x / 10;
            if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
            if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;

        }
        return rev;
    }
};