#include <vector>
using namespace std;
// 1..n 任意k个数的所有组合
class Solution {
vector<int>temp;
private:
    void search(vector<vector<int>>&result, int cur, int count, int n,int k) {
        if (count == k) {
            result.push_back(temp);
        }else
            for (int i=cur;i<n+1;i++) {
                temp.push_back(i);
                search(result, i+1, count+1, n, k);
                temp.pop_back();
            }
    }
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        search(result, 1, 0, n, k);
        return result;
    }
};