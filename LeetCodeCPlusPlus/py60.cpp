// 第k个排列，集合[1,2,...,n]的全排列按顺序编号
#include <string>
#include <vector>
#include <math.h>
// 解法找规律。算每种排列的个数，得出每一位数字
using namespace std;
class Solution {
public:
    int factorial(int j) {
        if (j == 1 || j == 0) return 1;
        else return j*factorial(j-1);
    }
    string getPermutation(int n, int k) {
        vector<char> nums;
        for (int i=1;i<n+1;i++)
            nums.push_back('0'+i);
        
        n--;
        string result="";
        while (n>-1) {
            int t = factorial(n);
            int pos = ceil(1.0*k/t) - 1;
            //cout<<n<<" "<<t<<" "<<k<<" "<<pos<<endl;
            pos = pos >= 0 ? pos:nums.size()-1;  // 出现-1的情况是k=0，逆序输出，k小于t时，ceil(0.x) = 1
            result.push_back(nums[pos]);
            nums.erase(nums.begin()+pos);
            k %= t;
            n--;
        }
        return result;
        
    }
};