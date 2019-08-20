#include <vector>
using namespace std;
class Solution {
public:
    //C++最简洁的二分法分类讨论
//每次二分，左半部分和右半部分至少有一边是有序的，以此为条件可以分成两种情况：
//1、左半边是有序的
//(1) target落在左半边
//(2) otherwise
//2、右半边是有序的
//(1) target落在右半边
//(2) otherwise
//综上所述，一共两种可能性，这两种情况各自又有两种可能性，代码如下：
bool search(vector<int>& nums, int target) {
        int l = 0, r = nums.size()-1;
        while(l<=r){
            //处理重复数字
            while(l<r&&nums[l]==nums[l+1]) ++l;
            while(l<r&&nums[r]==nums[r-1]) --r;
            int mid = l+(r-l)/2;
            if(nums[mid]==target) return true;
            //左半部分有序
            if(nums[mid]>=nums[l]){
                if(target<nums[mid]&&target>=nums[l]) r = mid-1;//target落在左半边
                else l = mid+1;
            }
            else{//右半部分有序
                if(target>nums[mid]&&target<=nums[r]) l = mid+1;//target落在右半边
                else r = mid-1;
            }
        }
        return false;
    }
};