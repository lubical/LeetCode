#include<vector>
using namespace std;

// 删除排序数组中的重复项。与前面的不同，为空则插入应该插入的位置，插入位置+1

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int index=0,result = 0;
        while (index<nums.size()) {
            if (index==0||nums[index]!=nums[index-1]) {
                nums[result++] = nums[index];
            }
            index++;
        }
        return result;
    }
};