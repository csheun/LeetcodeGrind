class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        for (int i = 0; i < strs.size(); i++) {
            string sorted_str = strs[i];
            sort(sorted_str.begin(), sorted_str.end());
            if (map.find(sorted_str) != map.end()) {
                map[sorted_str].push_back(strs[i]);
            } else {
                map[sorted_str] = {strs[i]};
            }
        }
        vector<vector<string>> res;
        for (const auto pair : map) {
            res.push_back(pair.second);
        }
        return res;
    }
};