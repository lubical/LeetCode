// 二进制求和
#include <string>
using namespace std;
class Solution {
public:
    string addBinary(string a, string b) {
        string s;
		s.reserve(a.size() + b.size());
		int c = 0, i = a.size() - 1, j = b.size() - 1;
		while(i >= 0 || j >= 0 || c == 1)
		{
			c += i >= 0 ? a[i--] - '0' : 0;
			c += j >= 0 ? b[j--] - '0' : 0;
			s.push_back((c & 1) + '0');
			c >>= 1;
		}
		reverse(s.begin(), s.end());
		return s;
    }
};