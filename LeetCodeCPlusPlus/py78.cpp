// 子集
#include <vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int> > dp(1);
        for(int i = 0; i < nums.size(); i++){
            int m = dp.size();
            for(int j = 0; j < m; j++){
                vector<int> tmp = dp[j];
                tmp.push_back(nums[i]);
                dp.push_back(tmp);
            }
        }
        return dp;
    }


};