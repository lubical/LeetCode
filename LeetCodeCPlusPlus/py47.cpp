// 全排列，有重复数字，不允许重复
#include <vector>
using namespace std;
class Solution {
    vector<int>tmp;
    vector<bool>used;
private:
    void dfs(vector<vector<int>>&result, vector<int>&nums, int index) {
         if (index==nums.size()) {
             result.push_back(tmp);
             return;
         }
        
        for (int i=0;i<nums.size();i++) 
            if (!used[i]) {
                if (i>0 && nums[i]==nums[i-1] && !used[i-1]) // 此处used[i-1]前加不加!代表两种情况，一种剪右支，一种剪左支
                    continue;
                used[i] = true;
                tmp.push_back(nums[i]);
                dfs(result, nums, index+1);
                tmp.pop_back();
                used[i] = false;
            }
        
    }
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        used.resize(nums.size());
        vector<vector<int>> result;
        dfs(result, nums, 0);
        return result;
    }
};