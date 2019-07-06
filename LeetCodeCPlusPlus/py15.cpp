#include <iostream>
#include <vector>
#include <map>
using namespace std;
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        map<int,int> intMap;
        map<int,int>::iterator iterL,iterR, iterC;
        for (int i=0;i<nums.size();i++) {
            if (intMap.count(nums[i]) == 0)
                intMap[nums[i]] = 1;
            else
                intMap[nums[i]] += 1;
        }
        
        for(iterL = intMap.begin(); iterL != intMap.end() && iterL->first<=0; iterL++) {
            iterL->second--;
            //cout<< iterL->first<<" "<< iterL->second <<endl;  
            iterR = intMap.end();
            iterR--;
            //cout<<"r: "<< iterR->first<<" "<<iterR->second<<endl;
            int center_key = 0 - iterL->first - iterR->first;
            while (iterL->first<=iterR->first && center_key <= iterR->first) {
                iterR->second--;
                iterC = intMap.find(center_key);
                if (iterC!=intMap.end() && iterC->second>0) {
                    result.push_back(vector<int>{iterL->first, center_key, iterR->first});
                }
                iterR->second++;
                if (iterL==iterR) //处理边界
                    break;
                iterR--;
                center_key = 0 - iterL->first - iterR->first;
            }
            iterL->second = 0;
        }
        return result;  
    }
};

int main(void) {
 
    vector<int> resource = {-5, -4, -3, -2, -1, 1, 2, 3};
    vector<vector<int>> ans = Solution().threeSum(resource);
    for (int i=0;i<ans.size();i++)
        cout<<ans[i][0]<<" "<<ans[i][1]<<" "<<ans[i][2]<<endl;
    return 0;
}