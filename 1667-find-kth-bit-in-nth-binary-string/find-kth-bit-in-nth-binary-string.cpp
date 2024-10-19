class Solution {
public:
    string invert(string s) {
        string res{""};
        for (char& c : s) {
            if (c == '1') {
                res += "0";
            } else {
                res += "1";
            }
        }
        return res;
    }
    string helper(int n) {
        if (n == 1) {
            return "0";
        }
        string s = helper(n - 1);
        string s_rev = invert(s);
        reverse(s_rev.begin(), s_rev.end());
        return s + "1" + s_rev;
    }
    char findKthBit(int n, int k) {
        string s = helper(n);
        return s[k - 1];
    }
};