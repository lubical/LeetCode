#include <vector>
#include <string>
#include <sstream>
#include <unordered_map>
using namespace std;
// 字母异位分词
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
         unordered_map<string, vector<string>> hashmap;
         for(auto s : strs){
             vector<int> tmp(26);
             for (auto ch : s)
                 tmp[ch-'a']++;
             std::stringstream ss;
             for (auto k : tmp)
                 ss<<k;
             hashmap[ss.str()].push_back(s);
             //string temp = s;
             //sort(temp.begin(), temp.end());
             //hashmap[temp].push_back(s);
             
         }
        int len = hashmap.size();
        vector<vector<string>> ans(len);
        int index = 0;
        for(auto i : hashmap){
            ans[index++] = i.second;
            //index;
        }
        return ans;

    }
};