class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_map<string, int> visited;
        deque<pair<string, int>> queue;
        string curr = "0000";
        queue.push_back({curr, 0});
        while (queue.size() > 0) {
            pair<string, int> item = queue.front();
            queue.pop_front();
            visited[item.first] =  item.second;
            auto it = std::find(deadends.begin(), deadends.end(), item.first);
            if (it == deadends.end()) {
                if (item.first == target) {
                    return item.second;
                }
            }
            else {
                continue;
            }
            vector<string> nextIter = generateNext(item.first);
            for (const string code : nextIter) {
                if (visited.find(code) == visited.end()) {
                    visited[code] = item.second + 1;
                    queue.push_back({code, item.second + 1});
                }
            }
        }
        return -1;
    }
    
    vector<string> generateNext(string code) {
        vector<string> res;
        for (int i = 0; i < 4; i++) {
            int num = code[i] - '0';
            int nextNum1 = (num + 1) % 10;
            int nextNum2 = (num + 10 - 1) % 10;
            string nextString1 = code;
            string nextString2 = code;
            nextString1[i] = nextNum1 + '0';
            nextString2[i] = nextNum2 + '0';
            res.push_back(nextString1);
            res.push_back(nextString2);
        }
        return res;
    }
};