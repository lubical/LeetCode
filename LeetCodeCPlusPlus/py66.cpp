// 加1
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int len = digits.size();
        int add_on = 1;
        for(int i=len-1;i>=0;i--) {
            digits[i] += add_on;
            if (digits[i]<10) {
                add_on = 0;
                break;
            }
            else {
                digits[i] -= 10;
                add_on = 1;
            }
        }
         
        if (add_on == 1) {
            vector<int> ans(len, 0);
            ans.insert(ans.begin(),1);
            return ans;
        } else
            return digits;
        
    }
};