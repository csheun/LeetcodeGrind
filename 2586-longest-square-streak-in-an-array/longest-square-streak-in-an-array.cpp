class Solution {
public:
    int squareroot(int num) {
        int res = static_cast<int>(sqrt(num));
        if (res * res == num) return res;
        else return -1;
    }
    int longestSquareStreak(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> streakCount(nums.size(), 0);
        unordered_map<int, int> map;
        int res = -1;
        for (int i = 0; i < nums.size(); ++i) {
            // find in map;
            // cout << "curr: " << nums[i] << '\n';
            int sqrt_res = squareroot(nums[i]);
            if (sqrt_res == -1) {
                map[nums[i]] = 1;
            } else {
                // find in map
                if (map.find(sqrt_res) != map.end()) {
                    // cout << "Found sqrt: " << sqrt_res << '\n';
                    // cout << "count: " << sqrt_res << '\n';
                    map[nums[i]] = map[sqrt_res] + 1;

                    if (map[nums[i]] > res) res = map[nums[i]];
                } else {
                    map[nums[i]] = 1;
                }
            }
        }
        return res;
    }
};