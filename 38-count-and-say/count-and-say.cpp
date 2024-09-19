class Solution {
public:
    string countAndSay(int n) {
        // base case
        if (n == 1) {
            return "1";
        }
        return calculate(countAndSay(n - 1));
    }

    string calculate(string s) {
        string res{};
        char prev{s[0]};
        int count{0};
        for (auto &ch : s) {
            if (ch == prev) {
                count += 1;
            } else {
                res += to_string(count);
                res += prev;
                prev = ch;
                count = 1; 
            }
        }
        res += to_string(count);
        res += s[s.length()-1];
        return res;
    }
};