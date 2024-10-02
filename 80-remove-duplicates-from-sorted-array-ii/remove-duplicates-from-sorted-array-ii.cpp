class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        unordered_map<int, int> dup_count;
        int fail_ptr{-1};
        int curr_ptr{0};
        for (int i = 0; i < nums.size(); i++) {
            if (dup_count[nums[i]] + 1 <= 2) {
                dup_count[nums[i]] += 1;
                if (fail_ptr != -1) {
                    //swap
                    int tmp = nums[i];
                    nums[i] = nums[fail_ptr];
                    nums[fail_ptr] = tmp;
                    fail_ptr++;
                }
            } else {
                if (fail_ptr == -1) {
                    fail_ptr = i;
                } 
            }
        }
        if (fail_ptr == -1) {
            return nums.size();
        } else {
            return fail_ptr;
        }
    }
};