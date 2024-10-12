class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        priority_queue<int, vector<int>, greater<int>> end;
        end.push(intervals[0][1]);
        for (int i = 1; i < intervals.size(); i++) {
            int earliest_end_time = end.top();
            if (intervals[i][0] <= earliest_end_time) {
                end.push(intervals[i][1]);
            } else {
                end.pop();
                end.push(max(earliest_end_time, intervals[i][1]));
            }
        }
        return end.size();
    }
};