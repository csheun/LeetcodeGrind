class Solution {
public:
    bool canJump(vector<int>& nums) {
        if (nums.size() == 1) return true;
        int max_distance = -1;
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] == 0) {
                // check if max distance can jump over me...
                if (max_distance <= i) return false; 
            }
            max_distance = max(max_distance, i + nums[i]);
            if (max_distance >= nums.size() - 1) return true;
        }
        return false;
    }
};