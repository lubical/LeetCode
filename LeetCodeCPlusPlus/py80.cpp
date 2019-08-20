// 删除数组中重复出现次数大于2次的值
#include <vector>
using namespace std;
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        int index = 1;
        int counts = 1;
        for (int i=1;i<nums.size();i++) {
            counts = nums[i] == nums[i-1] ? counts + 1 : 1;
            if (counts <= 2)
                nums[index++] = nums[i];
        }
        return index;
    }
};