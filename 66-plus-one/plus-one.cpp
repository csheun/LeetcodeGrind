class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        // loop through the digits from the back and +1
        // if = 10, then continue, else return;

        for (int i = digits.size() - 1; i >= 0; i--) {
            int curr = digits[i];
            int pres = curr + 1;
            if (pres != 10) {
                digits[i] = pres;
                return digits;
            } else {
                digits[i] = 0;
            }
        }
        if (digits[0] == 0) {
            digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};