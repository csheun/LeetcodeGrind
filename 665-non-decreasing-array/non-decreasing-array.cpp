class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        bool chance = true;
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                if (chance) {
                    if (i == 0) {
                        nums[i] = nums[i + 1];
                    } else {
                        if (nums[i + 1] < nums[i - 1]) nums[i + 1] = nums[i];
                        else {
                            nums[i] = min(nums[i], nums[i + 1]);
                            nums[i] = min(nums[i], nums[i + 1]);
                        }
                    }
                    chance = false;
                } else return false;
            }
        }
        return true;
    }
};