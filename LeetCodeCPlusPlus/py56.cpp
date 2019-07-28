// 合并区间，排序后合并
#include <vector>
using namespace std;
class Solution {
public:
    static bool cmp(const vector<int>&a,const vector<int>&b )
    {
        if(a[0]==b[0])
            return a[1]>b[1];
        return a[0]<b[0];
    }
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> result;
        if (intervals.empty())
            return result;
        sort(intervals.begin(), intervals.end(), cmp);
        int begin = intervals[0][0];
        int end = intervals[0][1];
        for (int i=0;i<intervals.size(); i++) {
            if (intervals[i][0]>end) {
                result.push_back({begin, end});
                begin = intervals[i][0];
                end = intervals[i][1];
            }else if (intervals[i][1]>end) 
                end = intervals[i][1];
        }
        result.push_back({begin,end});
        return result;
    }
};