class Solution {
public:
    int minLength(string s) {
        int res = s.size();
        string curr_str{s};
        while (true) {
            string new_str{""};
            int n = curr_str.size();
            int i = 0;
            bool removed = false;
            while (i < n - 1) {
                string curr = curr_str.substr(i, 2);
                if (curr == "AB" || curr == "CD") {
                    res -= 2;
                    i += 2;
                    removed = true;
                } else {
                    new_str += curr_str[i];
                    i++;
                }
            }
            if (!removed) {
                break;
            }
            if (i == n - 1) {
                new_str += curr_str[i];
            }
            curr_str = new_str;

        }
        return res;
    }
};