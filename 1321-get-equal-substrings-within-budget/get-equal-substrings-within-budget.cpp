class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int total_cost{};
        int left{0};
        int max_length{0};

        for (int right = 0; right < t.length(); right++) {
            int cost = abs(s[right]-t[right]);
            total_cost += cost;

            while (total_cost > maxCost) {
                total_cost -= abs(s[left]-t[left]);
                left +=1;
            }
            
            max_length = max(max_length, right - left + 1);
        }
        return max_length;
    }
};