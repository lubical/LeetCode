#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size()-1, ans;
        ans = (right-left)*min(height[right], height[left]);
        while (left<right) {
            if (height[left]<height[right]) 
                left++;
            else
                right--;
            ans = max(ans, (right-left)*min(height[right], height[left]));
        }
        return ans;
    }
};