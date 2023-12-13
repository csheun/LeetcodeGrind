class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> myMap;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (myMap.find(complement) != myMap.end()) {
                return {myMap[complement], i};
            } else {
                myMap[nums[i]] = i;
            }
        }
        return {};
    }
};