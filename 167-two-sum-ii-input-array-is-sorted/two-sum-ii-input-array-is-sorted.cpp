class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int leftPtr = 0;
        int rightPtr = numbers.size() - 1;

        while (leftPtr < rightPtr) {
            int sum = numbers[leftPtr] + numbers[rightPtr];
            if (sum == target) {
                return {leftPtr + 1, rightPtr + 1};
            } else if (sum < target) {
                leftPtr++;
            } else {
                rightPtr--;
            }
        }
        return {};
    }
};