// 字符串相乘
// 竖式相加即可
#include <string>
#include <vector>
// 字符串相乘；竖式乘法
using namespace std;
class Solution {
public:
    string multiply(string num1, string num2) {
        int n = num1.size(), m = num2.size();
        vector<int> result(n+m, 0);
        if (num1=="0" || num2=="0")
            return "0";
        // 计算后放到相应的位置；倒序的，从0开始的
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++) 
                result[m+n-(i+j)-2] += (num1[i]-'0') * (num2[j]-'0');
        // 累加并处理所有的结果
        for (int i=0;i<n+m-1;i++) {
            result[i+1] += result[i]/10;
            result[i] = result[i] % 10;
        }
        // 查找前导0
        int i = n+m-1;
        while (result[i] == 0 && i>0) i--;
        string ans = "";
        while (i>=0) {
            ans = ans + to_string(result[i--]);
            //cout<<result[i+1]<<" ";
        }
        return ans;
    }
};