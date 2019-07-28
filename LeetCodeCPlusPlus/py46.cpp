// 没有重复数字的全排列
#include <vector>
using namespace std;
class Solution {
private:
    void swap(int&a, int&b) {
        int tmp = a;
        a = b;
        b = tmp;
    }
    vector<int> tmp;
    void dfs(vector<vector<int>>&result, vector<int>&nums, int index) {
        if (index == nums.size()) {
            result.push_back(nums);
            return;
        }
        for (int i = index; i < nums.size(); i++) {
            swap(nums[i], nums[index]);
            dfs(result, nums, index+1);
            swap(nums[i], nums[index]);
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        dfs(result, nums, 0);
        return result;
    }
};