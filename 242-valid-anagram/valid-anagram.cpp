#include <unordered_map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        unordered_map<char, int> map;
        for (int i = 0; i < s.length(); i++) {
            map[s[i]] += 1;
        }
        for (int i = 0; i < t.length(); i++) {
            if (map.find(t[i]) == map.end()) {
                return false;
            } else {
                map[t[i]]--;
                if (map[t[i]] < 0) return false;
            }
        }
        return true;
    }
};