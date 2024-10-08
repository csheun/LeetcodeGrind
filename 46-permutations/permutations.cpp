class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        if (nums.size() == 1) {
            return {{nums[0]}};
        }
        for (int i = 0; i < nums.size(); i++) {
            vector<int> nums_copy = nums;
            nums_copy.erase(nums_copy.begin() + i);
            vector<vector<int>> inner_res = permute(nums_copy);
            for (auto& x : inner_res) {
                x.insert(x.begin(), nums[i]);
                res.push_back(x);
            }
        }
        return res;
    }
};