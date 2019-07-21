// 在排序数组中查找元素的第一个和最后一个位置
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if (nums.size()==0) return vector<int>{-1,-1};
        int n = nums.size();
        int i=0, j=n-1;
        while (i<j) {
            int mid = (i+j)>>1;
            if (nums[mid]>=target)
                j = mid;
            else
                i = mid+1;
        }
        if (nums[i] != target)
            return vector<int>{-1,-1};
        vector<int>result = {i};
        j = n-1;
        while (i<j) {
            int mid = (i+j+1)>>1;
            if (nums[mid]<=target)
                i = mid;
            else
                j = mid-1;
        }
        result.push_back(i);
        return result;
    }
};