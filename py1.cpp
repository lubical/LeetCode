#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> a(2);
        for(int i=0;i<nums.size()-1;i++)
            for (int j=i+1;j<nums.size();j++)
                if (nums[i]+nums[j] == target){
                    a[0] = i;
                    a[1] = j;
                    return a;
                }
             return a;       
    }
};
int main(){
    Solution solution = Solution();
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = (solution.twoSum(nums, target));
    for (int i=0;i<result.size();i++)
        cout<<result[i]<<" ";

    return 0;

}
