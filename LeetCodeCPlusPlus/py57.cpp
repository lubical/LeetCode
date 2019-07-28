// 给出一个无重叠，按照区间起始端点排序的区间列表，在列表中插入一个新的区间，确保仍然有序，不重叠
#include <vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> result;
        int i = 0;
        while (i<intervals.size() && intervals[i][1] < newInterval[0]) { // 之前的有序部分插入
            result.push_back(intervals[i]);
            i++;
        }
        while (i<intervals.size() && intervals[i][0] <= newInterval[1]) { // 那个需要合并的区间
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }
        result.push_back(newInterval);
        while(i<intervals.size()) // 剩下的部分
            result.push_back(intervals[i++]);
        return result;
    }
};