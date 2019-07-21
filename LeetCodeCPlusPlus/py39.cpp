// 组合总和等于target的所有情况，可重复使用
#include <vector>
using namespace std;
class Solution {
    vector<vector<int>> result;
    vector<int> tmp;
private: 
    void helper(vector<int>& candidates, int target, int index) {
        if (target<0 || index>=candidates.size() || target!=0 && target<candidates[index])
            return;
        if (target == 0) {
            result.push_back(tmp);
        } else {
            helper(candidates, target, index+1);
            tmp.push_back(candidates[index]);
            helper(candidates, target-candidates[index], index);
            tmp.pop_back();
        }
    
}
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        helper(candidates, target, 0);
        return result;
    }
};