// 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#include <vector>
using namespace std;
class Solution {
private:
    int leetcode84(vector<int>& nums) {
        vector<int>heights(nums);
        heights.insert(heights.begin(), 0);
        heights.insert(heights.end(), 0);
        vector<int> stack;
        int result = 0;
        for (int i=0;i<heights.size();i++) {
            while (!stack.empty() && heights[stack.back()] > heights[i]) {
                int top = stack.back();
                stack.pop_back();
                result = max(result, (i-stack.back()-1)*heights[top]);
            }
            stack.push_back(i);
        }
        return result;
    }
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        vector<int>dp(matrix[0].size());
        int maxarea = 0;
        for (int i=0;i<matrix.size();i++) {
            for (int j=0;j<matrix[0].size();j++)
                dp[j] = matrix[i][j] == '1' ? dp[j]+1 : 0;
            maxarea = max(maxarea, leetcode84(dp));
        }
        return maxarea;
            
    }
};