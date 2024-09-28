class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        if (nums.size() < 3) {
            return -1;
        }
        sort(nums.begin(), nums.end());

        long long sum = nums[0] + nums[1];
        long long max_p = 0;

        for (int i = 2; i < nums.size(); i++) {
            if (sum > nums[i]) {
                max_p = sum + nums[i];
            } 
            sum += nums[i];
        }

        return max_p == 0 ? -1 : max_p;
    }
};