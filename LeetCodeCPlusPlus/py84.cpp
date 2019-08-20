/**
 * 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
 *  求在该柱状图中，能够勾勒出来的矩形的最大面积。
 * 
 * 解法：以第i个柱子为最低的矩形面积是找到左右两边比heights[i]小的第一个heights[left_i], heights[right_i]
 *      面积为 (right_i - left_i - 1) * heights[i]
 *  单调栈
 */
#include <vector>
using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
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
};