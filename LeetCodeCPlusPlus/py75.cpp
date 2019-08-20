/*
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
解法：左右指针，注意0的时候只要移动右指针，0的时候才要移动左指针
 */
#include <vector>
using namespace std;
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int right = nums.size() - 1;
        if (right<1)
            return;
        int index = 0, left = 0, temp;
        while(index<=right) {
            while (nums[index] != 1 && index>=left && index<=right) {
                if (nums[index] == 2) {
                    temp = nums[index];
                    nums[index] = nums[right];
                    nums[right] = temp;
                    right--;
                }else if(nums[index] == 0) {
                    temp = nums[index];
                    nums[index] = nums[left];
                    nums[left] = temp;
                    left++;
                }
            }
            index++;
        }
    }
};