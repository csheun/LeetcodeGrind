// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int i = 1;
        int j = n;
        while (i <= j) {
            int mid = i + (j - i) / 2;
            if (isBadVersion(mid)) {
                if (mid == 1) return 1;
                if (! isBadVersion(mid - 1)) return mid;
                j = mid - 1;
            } else {
                i = mid + 1;
            }
        }
        return -1;
    }
};