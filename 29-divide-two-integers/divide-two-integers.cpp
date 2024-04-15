class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == divisor) {
            return 1;
        }
        bool sign = true;
        if ((dividend <= 0 && divisor > 0) || (dividend >= 0 && divisor < 0)) {
            sign = false;
        }
        long n = abs(dividend); 
        long m = abs(divisor);
        long res = 0;

        while (n >= m) {
            int count = 0;

            while (n >= (m << count)) {
                count++;
            }
            res += 1 << (count - 1);

            n -= m << (count - 1);
        }
        if (res == (1<<31)) {
            return sign ? INT_MAX : INT_MIN;
        }
        return sign ? res : res * -1;        
    }
};