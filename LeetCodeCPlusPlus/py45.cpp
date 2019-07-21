// 跳跃游戏，贪心，跳得最远
#include <vector>
using namespace std;
class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        if (n < 2)
            return 0;
        int step = 0;
        int pos = 0;
        int max_pos = 0;
        for (int i=0;i<n;i++) {
            if (pos+nums[pos]<i) {
                pos = max_pos;
                step++;
                // cout<<pos<<" "<<step<<endl;
            }
            if (i+nums[i]>=max_pos+nums[max_pos])
                max_pos = i;
        }
        return step+1;  // 最后一次没有走过边界，因此要总的步数再加1
    }
};