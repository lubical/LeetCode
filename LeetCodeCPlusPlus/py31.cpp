class Solution {
private:
    void swap(int &a, int &b) {
        int tmp = a;
        a = b;
        b = tmp;
    }
    void reverse(vector<int>& nums, int left, int right) {
        while (left<right) {
            swap(nums[left++], nums[right--]);
        }
    }
public:
    void nextPermutation(vector<int>& nums) {
        
        int n = nums.size() - 1;
        int index = n;
        while (index>0 && nums[index] <= nums[index-1])
            index--;
        
        if (index > 0) {
            for (int j=n;j>index-1;j--)
                if (nums[j] > nums[index-1]) {
                    swap(nums[index-1], nums[j]);
                    break;
                }
            reverse(nums, index, n);
        }
        else
            reverse(nums, 0, n);
    }
};