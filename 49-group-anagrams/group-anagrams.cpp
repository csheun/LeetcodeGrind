class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        vector<unordered_map<char, int>> mps;
        for (string str : strs) {
            unordered_map<char, int> mp;
            for (char c : str) {
                mp[c]++;
            }
            // check with all other mps
            int match = -1;
            for (int i = 0; i < mps.size(); i++) {
                if (mps[i] == mp) {
                    match = i;
                    break;
                }
            }
            if (match != -1) {
                result[match].push_back(str);
            } else {
                // include hashmap and new str
                mps.push_back(mp);
                result.push_back({str});
            }
        }
        return result;
    }
};