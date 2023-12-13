class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        vector<int> workingVector = nums;
        sort(workingVector.begin(), workingVector.end());
        int left_ptr = 0;
        int right_ptr = workingVector.size() - 1;
        while (left_ptr < right_ptr) {
            int sum = workingVector[left_ptr] + workingVector[right_ptr];
            if (sum == target) {
                break;
            } else if (sum < target) {
                left_ptr += 1;
            } else {
                right_ptr -= 1;
            }
        }
        auto left = std::find(nums.begin(), nums.end(), workingVector[left_ptr]);
        int index = std::distance(nums.begin(), left);
        result.push_back(index);
        auto right = std::find(nums.begin(), nums.end(), workingVector[right_ptr]);
        if (workingVector[left_ptr] == workingVector[right_ptr]) {
            right = std::find(left + 1, nums.end(), workingVector[right_ptr]);
        }
        index = std::distance(nums.begin(), right);
        result.push_back(index);
        return result;
    }
    
};