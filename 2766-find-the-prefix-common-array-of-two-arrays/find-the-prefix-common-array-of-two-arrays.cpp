class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        int size = A.size();
        vector<int> numbers(size, 2);
        vector<int> res(size);
        int lastCount = 0;
        for (int i = 0; i < size; i++) {
            numbers[(A[i] - 1)]--;
            if (numbers[(A[i] - 1)] == 0) {
                lastCount++;
            }
            numbers[(B[i] - 1)]--;
            if (numbers[(B[i] -  1)] == 0) {
                lastCount++;
            }
            res[i] = lastCount;
        }
        return res;
    }
};