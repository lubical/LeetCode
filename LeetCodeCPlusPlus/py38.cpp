// 报数1， 11， 21， 1211; 递推
#include <string>
using namespace std;
class Solution {
public:
    string countAndSay(int n) {
        
        if (n==1)
            return "1";
        
        string last="1";
        for (int i = 1;i<n;i++) {
            int index = 0;
            string now="";
            while (index<last.size()) {
                char ch = last[index];
                int count = 1;
                while (index<last.size()-1 && last[index]==last[index+1]) {
                    count++;
                    index++;
                }
                now = now + to_string(count) + ch;
                //cout<<now<<endl;
                index++;
            }
            last = now;
        }
        return last;
    }
};