class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        unordered_map<int, int>remainder_count_map;
        int mid{0};
        if (k % 2 == 0) {
            mid = k / 2;
        }
        for (int num : arr) {
            int remainder = num % k;
            remainder_count_map[remainder] += 1;
        }
        auto og_map = remainder_count_map;
        for (auto& x : og_map) {
            int key = x.first;
            if (remainder_count_map[key] == -1) {
                continue;
            }
            if (key == 0) {
                if (x.second % 2 != 0) {
                    return false;
                }
            } else if (key == mid || key == -mid) {
                if ((remainder_count_map[mid] + remainder_count_map[-mid]) % 2 != 0) {
                    return false;
                }
                remainder_count_map[mid] = -1;
                remainder_count_map[-mid] = -1;
            } else {
                int x_1 = abs(key);
                int x_2 = k - x_1;
                if (remainder_count_map[x_1] + remainder_count_map[-x_2] != remainder_count_map[-x_1] + remainder_count_map[x_2]) {
                    return false;
                }
                remainder_count_map[x_1] = -1;
                remainder_count_map[x_2] = -1;
                remainder_count_map[-x_1] = -1;
                remainder_count_map[-x_2] = -1;
            }
        }
        return true;
    }
};