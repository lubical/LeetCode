#include<iostream>
using namespace std;
class Solution {
public:
    bool checkPalindrome(string s, int i, int j) {
        if (j>s.size()) return false;
        while (i<j) {
            if (s[i] != s[j]) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    string longestPalindrome(string s) {
        int low = 0, high = s.size(), mid;
        string ans;
        if (s == ""|| s.size() == 1) 
            return s;
    
        while (low<=high) {
            mid = (low+high)/2;
            bool changed = false;
            for (int i=0;i<s.size()-mid;i++) {
                if (checkPalindrome(s, i, i+mid-1)){
                    changed = true;
                    ans = s.substr(i, mid);
                    break;
                }
            }
            for (int i=0;i<s.size()-mid;i++) {  
                if (checkPalindrome(s, i, i+mid)){
                    changed = true;
                    ans = s.substr(i, mid+1);
                    break;
                }
            }
            
            if (!changed) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
            
        }
        return ans;
    }
};
int main(int argc, char *argv[])
{
	string resource = "aaaa";
	
	Solution solution;
	string ret = solution.longestPalindrome(resource);
    cout<<ret<<endl;
	return 0;
}