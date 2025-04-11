class Solution {
public:
    int countSymmetricIntegers(int low, int high) {
        int res = 0;
        for (int i = low; i < high + 1; ++i) {
            if (isSymmetric(i)) {
                res++;
            }
        }
        return res;
    }

    bool isSymmetric(int target) {
        string target_str = to_string(target);
        int len = target_str.length();
        if (len % 2 != 0) return false;
        int sum = 0;
        int symSum = 0;
        for (int i = 0; i < len; ++i) {
            sum += target_str[i] - '0';
            if (i < len / 2) {
                symSum += target_str[i] - '0';
            }
        }
        if (sum % 2 != 0) return false;
        return (sum / 2) == symSum;
    }
};