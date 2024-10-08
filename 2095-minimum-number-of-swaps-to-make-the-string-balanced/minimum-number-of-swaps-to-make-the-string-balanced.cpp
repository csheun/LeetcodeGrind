class Solution {
public:
    int minSwaps(string s) {
        int swap_count{0}, left{0}, right{int(s.length()) - 1};
        int left_open{0}, left_close{0}, right_open{0}, right_close{0};

        while (left < right) {
            while (left_open >= left_close) {
                if (s[left] == '[') left_open++; else left_close++;
                left++;
                if (left >= s.length()) {
                    return swap_count;
                }
            }
            while (right_close >= right_open) {
                if (s[right] == '[') right_open++; else right_close++;
                right--;
                if (right < 0) {
                    return swap_count;
                }
            }
            cout << "left: " << left << '\n';
            cout << "right: " << right << '\n';
            // swap
            s[left - 1] = '[';
            s[right + 1] = ']';
            swap_count++;
            left_open++;
            left_close--;
            right_open--;
            right_close++;
        }
        return swap_count;
    }
};