class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        std::unordered_map<char, int> mp;
        for (char c : s) {
            mp[c]++;
        }
        for (char c: t) {
            if (mp.find(c) == mp.end() || mp[c] == 0) {
                return false;
            }
            mp[c] -= 1;
        }
        return true;
    }
};