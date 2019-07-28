// 最大子序和
// 和大于0保留，小于0重新开始。
#include <vector>
using namespace std;
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max = -2147483648,total=0;
        for (int i=0;i<nums.size();i++) {
            total += nums[i];
            max = total>max? total: max;
            if (total<0) total = 0;
        }
        return max;
    }
};