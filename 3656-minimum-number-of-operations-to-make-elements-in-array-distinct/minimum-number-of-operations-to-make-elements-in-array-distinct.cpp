class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        unordered_map<int, bool> num_bool;
        int i;
        for (i = nums.size() - 1; i >= 0; --i) {
            if (num_bool.find(nums[i]) == num_bool.end()) {
                num_bool[nums[i]] = true;
            } else {
                // repeat
                break;
            }
        }

        if (i != -1) {
            // 'i' will the pos of the idx that repeats
            return ceil((i + 1) / 3.0);
        }
        return 0;
    }
};