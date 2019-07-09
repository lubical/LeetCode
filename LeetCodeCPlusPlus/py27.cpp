#include<vector>
using namespace std;
// 删除指定的元素，不使用额外的空间。
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int left = 0, right = nums.size()-1;
        while (left <= right) {
            if (nums[left] == val) {
                nums[left] = nums[right--];
            }else
                left++;
        }
        return left;
    }
};