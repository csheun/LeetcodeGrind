class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        unordered_map<int, bool> num_map;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] < k) return -1;
            if (nums[i] > k) {
                num_map[nums[i]] = true;
            }
        }
        return num_map.size();

    }
};