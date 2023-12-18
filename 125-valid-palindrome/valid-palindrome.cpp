#include <cctype>

class Solution {
public:
    bool isPalindrome(string s) {
        int leftPtr = 0;
        int rightPtr = s.size();
        while (leftPtr < rightPtr) {
            char leftChar = s[leftPtr];
            char rightChar = s[rightPtr];
            if (isalnum(leftChar) && isalnum(rightChar)) {
                if (tolower(leftChar) == tolower(rightChar)) {
                    leftPtr++;
                    rightPtr--;
                    continue;
                } else {
                    return false;
                }
            }
            if (!isalnum(leftChar)) {
                leftPtr++;
            }
            if (!isalnum(rightChar)) {
                rightPtr--;
            }
        }
        return true;
    }
};