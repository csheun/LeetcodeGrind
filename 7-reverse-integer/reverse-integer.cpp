class Solution {
public:
    int reverse(int x) {
        if (x == 0) {
            return 0;
        }
        if (x == INT_MIN) {
            return 0;
        }
        bool sign = true;
        if (x < 0) {
            sign = false;
        }
        string res_str = "";
        string x_str = to_string(x);
        int len = x_str.length();
        if (x_str[len - 1] != '0') {
            res_str += x_str[len - 1];
        }
        for (int i = len - 2; i >= 0; i--) {
            char target = x_str[i];
            if (target != '-') {
                res_str += target;
            }
        }
        if (!sign) {
            res_str = "-" + res_str;
            if (res_str.length() >= to_string(INT_MIN).length() &&res_str > to_string(INT_MIN)) {
                cout << to_string(INT_MIN) << endl;
                cout << res_str << endl;
                cout << "readch1";
                return 0;
            }
        } else {
            if (res_str.length() >= to_string(INT_MAX).length() && res_str > to_string(INT_MAX)) {
                cout << to_string(INT_MAX) << endl;
                cout << res_str << endl;
                cout << "readch2";
                return 0;
            }
        }

        return stoi(res_str);
    }
};