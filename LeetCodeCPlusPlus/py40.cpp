// 组合总数II，数字和等于target，不可重复；
// 思路：回溯，排序，同一层级里不允许使用两个相同的数
#include<vector>
using namespace std;
class Solution {
private:
    vector<int> tmp;
    int n;
    void helper(vector<int>& candidates, int index, int target, vector<vector<int>>& result) {
        if (target == 0) {
            result.push_back(tmp);
        }else {
            for (int i=index;i<n;i++) {
                if (i>index && candidates[i] == candidates[i-1])  // 同一层级的递归里不允许选择相同的项
                    continue;
                if (candidates[i] <= target) {
                    tmp.push_back(candidates[i]);
                    helper(candidates, i+1, target-candidates[i], result);
                    tmp.pop_back();
                }else
                    break;
            }
        }
    }
    
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        sort(candidates.begin(), candidates.end());
        n = candidates.size();
        helper(candidates, 0, target, result);
        return result;
    }
};