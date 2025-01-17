class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int size = nums.size();
        vector<int> prefix(size, 0);
        vector<int> suffix(size, 0);
        for (int i = 0; i < size; i++) {
            if (i == 0) {
                prefix[i] = 1;
                suffix[size - 1] = 1;
            } else {
                prefix[i] = nums[i - 1] * prefix[i - 1];
                suffix[size - 1 - i] = nums[size - i] * suffix[size - i];
            }
        }
        vector<int> res;
        for (int i = 0; i < size; i++) {
            res.push_back(prefix[i] * suffix[i]);
        }
        return res;
    }
};