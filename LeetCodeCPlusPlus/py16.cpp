#include <iostream>
#include <vector>
using namespace std;
// 三数之和最接近target，排序，固定左端，双指针遍历判断
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int n = nums.size();
        int ans = nums[0] + nums[1] + nums[2];
        for (int i=0; i<n-2;i++) {
            if (i>0 && nums[i]==nums[i-1])
                continue;
            int left = i + 1;
            int right = n - 1;
            while (left<right) {
                int cur = nums[i] + nums[left] + nums[right];
                if (cur == target)
                    return target;
                if (abs(cur-target) < abs(ans-target))
                    ans = cur;
                if (cur < target)
                    left++;
                else
                    right--;

            }
        }
        return ans;
    }
};