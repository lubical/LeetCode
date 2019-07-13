#include <vector>
using namespace std;
// logn时间内搜索不重复的旋转排序数组中的元素
class Solution {
public:
     // 由于任意一点的两测必定有一侧是有序的，因此可以直接二分。
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left<=right) {
            int mid = (left+right)>>1;
            if (nums[mid] == target)
                return mid;
            
            if (nums[mid]<nums[right]) { //旋转点在左侧，右侧有序
                if (target>nums[mid] && target <= nums[right])
                    left = mid + 1;
                else
                    right = mid - 1;
            } else {
                if (target>=nums[left] && target<nums[mid])
                    right = mid - 1;
                else
                    left = mid + 1;
            }
        }
        return -1;
    }
};