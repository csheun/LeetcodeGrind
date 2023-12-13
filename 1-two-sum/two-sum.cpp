class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> myMap;
        for (size_t i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (myMap.find(complement) != myMap.end()) {
                return {myMap[complement], static_cast<int>(i)};
            } else {
                myMap[nums[i]] = static_cast<int>(i);
            }
        }
        return {-1, -1};
    }
};