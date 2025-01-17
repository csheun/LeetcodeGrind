#include <unordered_map>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        for (const int num : nums) {
            map[num]++;
        }
        vector<pair<int,int>> vec;
        for (const auto pair : map) {
            vec.push_back({pair.second, pair.first});
        }
        sort(vec.begin(), vec.end(), [](pair<int, int>&a, pair<int, int>&b) {
            return a.first > b.first;
        });
        vector<int> res;
        for (int i = 0; i < k; i++) {
            res.push_back(vec[i].second);
        }
        return res;
    }
};