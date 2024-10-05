class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        vector<int> rem(k, 0);
        int count = 0;
        
        for(int& i : arr){
            int r = ((i % k) + k) % k;
            if (rem[r] > 0) {
                count++;
                rem[r]--;
            } else {
                rem[(k - r) % k]++;
            }
        }
        return count == (arr.size() / 2);
    }
};