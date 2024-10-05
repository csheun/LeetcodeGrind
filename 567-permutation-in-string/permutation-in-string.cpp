class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> s1_map;
        for (char c : s1) {
            s1_map[c] += 1;
        }
        int remaining = s1.size();
        int start_ptr{-1};
        for (int i = 0; i < s2.size(); i++) {
            cout << "start_ptr: " << start_ptr << '\n';
            char curr_char = s2[i];
            if (s1_map.find(curr_char) == s1_map.end()) {
                // cout << "can find\n";
                // add back all the char;
                remaining = s1.size();
                if (start_ptr != -1) {
                    for (int j = start_ptr; j < i; j++) {
                        s1_map[s2[j]] += 1;
                    }
                    start_ptr = -1;
                }

            } else {
                // can find

                if (s1_map[curr_char] != 0) {
                    s1_map[curr_char] -= 1;
                    remaining -= 1;
                    cout << "remaining: " << remaining << '\n';
                    if (remaining == 0) {
                        return true;
                    }
                    if (start_ptr == -1) {
                        // move start_ptr here
                        start_ptr = i;
                    }
                } 
                else {
                    // no slot -> move start ptr until valid;
                    while (true) {
                        bool cond = s2[start_ptr] == curr_char;
                        s1_map[s2[start_ptr]] += 1;
                        remaining += 1;
                        start_ptr += 1;
                        if (cond)
                            break;
                    }
                    s1_map[curr_char] -= 1;
                    remaining -= 1;
                    if (remaining == 0) {
                        return true;
                    }
                }
            }
        }
        return false;

    }
};