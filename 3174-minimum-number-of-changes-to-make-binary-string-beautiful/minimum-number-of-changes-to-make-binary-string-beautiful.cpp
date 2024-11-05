class Solution {
public:
    int minChanges(string s) {
        int res{0};
        char prev = s[0];
        int count{0};
        for (char c : s) {
            if (c == prev) {
                count += 1;
            } else {
                if (count % 2 == 0) {
                    // even -> move on
                    prev = c;
                    count = 1;
                } else {
                    res += 1;
                    count += 1;
                }
            }
        }
        return res;
    }
};