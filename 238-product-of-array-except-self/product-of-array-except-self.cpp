class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int arrSize = nums.size();
        vector<int> prefixArr(arrSize, 0);
        vector<int> suffixArr(arrSize, 0);
        for (int i = 0; i < arrSize; i++) {
            if (i == 0) {
                prefixArr[i] = 1;
                suffixArr[arrSize - 1 - i] = 1;
                continue;
            }
            prefixArr[i] = prefixArr[i - 1] * nums[i - 1];
            suffixArr[arrSize - 1 - i] = suffixArr[arrSize - i] *  nums[arrSize - i];
        }
        vector<int> res(arrSize, 1);
        for (int i = 0; i < arrSize; i++) {
            res[i] = prefixArr[i] * suffixArr[i];
        }
        return res;
    }
};