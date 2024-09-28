class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int res = INT_MIN;
        int left{0};
        int right{0};
        int curr_sum{0};
        while (right < n) {
            curr_sum += nums[right];
            res = max(res, curr_sum);
            while (curr_sum < 0) {
                curr_sum -= nums[left];
                left++;
            }
            right++;
        }
        return res;
    }
};