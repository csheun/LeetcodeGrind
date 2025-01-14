#include <unordered_map>
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, bool> map;
        for (int num : nums) {
            if (map.find(num) != map.end()) {
                return true;
            }
            map[num] = true;
        }
        return false;
    }
};