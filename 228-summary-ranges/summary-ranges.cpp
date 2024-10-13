class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        if (nums.size() == 0) {
            return {};
        }
        vector<string> res;
        int start = nums[0];
        int prev = nums[0];
        int end = nums[0];
        string str = to_string(start);
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == prev + 1) {
                end = nums[i];
                prev += 1;
            } else {
                if (start != end) {
                    str = str + "->" + to_string(end);
                }
                res.push_back(str);
                str = to_string(nums[i]);
                start = nums[i];
                prev = nums[i];
                end = nums[i];
            }
        }
        if (start != end) {
            str = str + "->" + to_string(end);
        }
        res.push_back(str);
        return res;
    }
};