class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        set<int> mySet;
        vector<int> res;
        unordered_map<int, int> myMap;
        for (int x : arr) {
            mySet.insert(x);
        }
        auto it = mySet.begin();
        for (int i = 0; i < mySet.size(); i++) {
            myMap[*it] = i;
            it++;
        }

        for (int x : arr) {
            res.push_back(myMap[x] + 1);
        }
        return res;
    }
};