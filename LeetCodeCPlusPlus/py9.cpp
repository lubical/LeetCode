// 回文数
class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0 || x%10==0 && x!=0)
            return 0;
        int ans = 0;
        while (ans<x) {
            ans = ans * 10 + x % 10;
            x = x/10;
        }
        if (ans == x || ans/10==x)
            return 1;
        else
            return 0;
    }
};