class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        vector<pair<int,int>> vec;
        for (int i = 0; i < nums.size(); i++) {
            vec.push_back(make_pair(nums[i], i));
        }
        sort(vec.begin(), vec.end());
        pair<int, int> prev = vec[0];
        for (int i = 1; i < vec.size(); i++) {
            if (vec[i].first == prev.first) {
                if (abs(vec[i].second - prev.second) <= k) {
                    return true;
                }
            }
            prev = vec[i];
        }
        return false;

    }
};