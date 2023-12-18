class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int arrSize = nums.size();
        vector<int> res(arrSize, 1);
        int prevP, prevS;
        for (int i = 0; i < arrSize; i++) {
            if (i == 0) {
                res[i] *= 1;
                prevP = 1;
                res[arrSize - 1 - i] *= 1;
                prevS = 1;
                continue;
            }
            prevP *= nums[i - 1];
            res[i] *= prevP;
            prevS *= nums[arrSize - i];
            res[arrSize - 1 - i] *= prevS;
        }
        return res;
    }
};