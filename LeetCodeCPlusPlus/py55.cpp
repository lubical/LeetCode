// 跳跃游戏，能否到达最后的位置
// 不断更新可达的最远位置，直至到最后或者不可达
#include <vector>
using namespace std;
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int index = 0;
        int furthest = 0;
        while (index<=furthest) {
            furthest = furthest>index+nums[index] ? furthest: index+nums[index];
            index++;
            if (furthest >= nums.size()-1)
                return true;
        }
        return false;
    }
};