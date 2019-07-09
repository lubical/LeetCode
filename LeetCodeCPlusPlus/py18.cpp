#include <vector>
using namespace std;
class Solution {
public:
    // 四数和为给定值，固定左边两个值，两个指针扫描，可剪枝。
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> ans;
        sort(nums.begin(),nums.end());
        int n = nums.size();
        for(int i=0;i<n-3;i++) {
            if (i>0 && nums[i] == nums[i-1])
                continue;
            if (nums[i]+nums[n-3]+nums[n-2]+nums[n-1]< target)
                continue;
            if (nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target)
                break;
            for(int j=i+1;j<n-2;j++) {
                if (j>i+1 && nums[j]==nums[j-1])
                    continue;
                int left = j+1, right = n-1;
                while (left<right) {
                    int cur = nums[i]+nums[j]+nums[left]+nums[right];
                    if (cur == target) 
                        ans.push_back({nums[i], nums[j], nums[left], nums[right]});
                    if (cur < target) {
                        left++;
                        while(left<right && nums[left]==nums[left-1]) left++;
                    } else {
                        right--;
                        while(left<right && nums[right]==nums[right+1]) right--;
                    }
                }
            }
        }
        return ans;
        
    }
};