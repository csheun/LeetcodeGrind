class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int count = 0;
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (visited[i][j] || grid[i][j] == '0') 
                    continue;
                count += 1;
                bfs(grid, visited, i, j);
            }
        }
        return count;
    }
    void bfs(vector<vector<char>>& grid , vector<vector<bool>>& visited, int i, int j) {
        int n_row = grid.size();
        int n_col = grid[0].size();
        queue<pair<int, int>> q;
        q.push({i,j});
        while (!q.empty()) {
            auto target = q.front();
            int row = target.first;
            int col = target.second;
            if (row - 1 >= 0) {
                if (!visited[row-1][col] && grid[row - 1][col] == '1') {
                    visited[row - 1][col] = true;
                    q.push({row - 1, col});
                }
            }
            if (row + 1 < n_row) {
                if (!visited[row + 1][col] && grid[row + 1][col] == '1') {
                    visited[row + 1][col] = true;
                    q.push({row + 1, col});
                }
            }
            if (col - 1 >= 0) {
                if (!visited[row][col - 1] && grid[row][col - 1] == '1') {
                    visited[row][col - 1] = true;
                    q.push({row, col - 1});
                }
            }
            if (col + 1 < n_col) {
                if (!visited[row][col + 1] && grid[row][col + 1] == '1') {
                    visited[row][col + 1] = true;
                    q.push({row, col + 1});
                }
            }
            q.pop();
        }
    }
};