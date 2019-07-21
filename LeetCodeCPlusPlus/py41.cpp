// 缺失的最小正数
// 桶排序，借助原有的数组空间
#include <vector>
using namespace std;
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for(int i=0;i<n;i++) {
            while (1<=nums[i]&&nums[i]<=n && nums[nums[i]-1]!=nums[i]) {
                int tmp = nums[i];
                nums[i] = nums[tmp-1];
                nums[tmp-1] = tmp;
            }
        }
        int i = 0;
        while(i<n && nums[i]==i+1)
            i++;
        return ++i;
    }
};