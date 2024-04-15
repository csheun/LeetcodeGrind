class Solution {
public:
    int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        int minus1, minus2;
        minus2 = 1;
        minus1 = 2;
        for (size_t i = 2; i < n; i++) {
            int temp = minus1 + minus2;
            minus2 = minus1;
            minus1 = temp;
        }
        return minus1;
    }
};