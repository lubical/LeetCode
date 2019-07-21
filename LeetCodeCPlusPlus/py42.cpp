// 接雨水； 由外向内，两侧边界保证可以接到雨水，移动小的边界与自身最大之差即为可接雨水
#include <vector>
using namespace std;
class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int left_max = 0, right_max = 0, ans = 0;
        while (left<right) {
            if (height[left]<height[right]) {
                if (height[left]>left_max) left_max = height[left];
                else ans += left_max-height[left];
                left++;
            }else {
                if (height[right]>right_max) right_max = height[right];
                else ans += right_max-height[right];
                right--;
            }
        }
        return ans;
    }
};