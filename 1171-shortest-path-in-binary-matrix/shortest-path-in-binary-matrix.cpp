class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] != 0 || grid[n - 1][n - 1] != 0) {
            return -1;
        }
        if (n == 1) {
            return 1;
        }
        vector<vector<bool>> visited(n, vector<bool>(n, false));
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {-1, -1}, {1, 1}, {0, -1}, {0, 1}, {-1, 1}, {1, -1}};
        queue<vector<int>> q;
        q.push({0 , 0, 1});
        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            for (auto& dir : directions) {
                int row = curr[0] + dir.first;
                int col = curr[1] + dir.second;

                if (row >= 0 && row < n && col >=0 && col < n && grid[row][col] == 0 && !visited[row][col]) {
                    visited[row][col] = true;
                    if (row == n - 1 && col == n - 1) {
                        return curr[2] + 1;
                    }
                    q.push({row, col, curr[2] + 1});
                }

            }
        }
        return -1;
    }
};