class Solution {
public:
    string makeFancyString(string s) {
        string res{""};
        char curr_c{' '};
        int count{0};

        for (char c : s) {
            if (c != curr_c) {
                res += c;
                curr_c = c;
                count = 1;
            } else {
                if (count != 2) {
                    res += c;
                    count += 1;
                }
            }
        }
        return res;
    }
};