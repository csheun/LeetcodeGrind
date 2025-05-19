class Solution {
public:
    string triangleType(vector<int>& nums) {
        bool tri = nums[0] + nums[1] > nums[2] && nums[0] + nums[2] > nums[1] && nums[2] + nums[1] > nums[0];
        if (!tri) return "none";
        if (nums[0] == nums[1] && nums[1] == nums[2]) {
            return "equilateral";
        } else if (nums[0] != nums[1] && nums[0] != nums[2] && nums[1] != nums[2]) {
            return "scalene";
        } else {
            return "isosceles";
        }
    }
};