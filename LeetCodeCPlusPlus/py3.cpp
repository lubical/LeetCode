#include<iostream>
#include<string>
#include<set>
using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char> myset;
        int i=0,j=0, n = s.size(), ans=0, result=0;
        while(i<n and j<n) {
            if (myset.count(s[j])==0) {
                myset.insert(s[j++]);
                result = max(result,j-i);
            } else {
                myset.erase(s[i++]);
            }
        }
       return result;
    }
};

int main(){
    Solution solution = Solution();
    string source = "abcabcccd";
    cout << solution.lengthOfLongestSubstring(source)<<endl;
    return 0;
}