class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        int n = skill.size();
        sort(skill.begin(), skill.end());
        int target_sum = skill[0] + skill[n - 1];
        long long chemistry = 0;
        for (int i = 0; i <= (n / 2) - 1; i++) {
            int sum = skill[i] + skill[n - 1 - i];
            if (sum == target_sum) {
                long long product = skill[i] * skill[n - 1 - i];
                chemistry += product;
            } else {
                return -1;
            }
        }
        return chemistry;
    }
};