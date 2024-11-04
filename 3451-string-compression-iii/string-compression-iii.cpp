class Solution {
public:
    string compressedString(string word) {
        string comp{""};
        int count{0};
        char prev = word[0];

        for (char c : word) {
            if (c != prev) {
                comp += to_string(count);
                comp += prev;
                count = 1;
                prev = c;
            } else {
                if (count == 9) {
                    comp += to_string(count);
                    comp += prev;
                    count = 0;
                }
                count += 1;
            }
        }
        comp += to_string(count);
        comp += prev;

        return comp;
    }
};