class Solution {
public:
	int helper(vector<vector<int>>& grid, vector<vector<int>>& visited, int row, int col) {
		int curr = grid[row][col];
		vector<pair<int,int>> directions = {{-1, 1}, {0, 1}, {1, 1}};
		int res = 0;
		for (auto dir : directions) {
			int new_row = row + dir.first;
			int new_col = col + dir.second;
			if (new_row >= 0 && new_row < grid.size() && new_col >= 0 && new_col < grid[0].size()) {
				if (grid[new_row][new_col] > curr) {
					if (visited[new_row][new_col] != -1) {
						res = max(res, visited[new_row][new_col] + 1);
					} else {
						res = max(res, helper(grid, visited, new_row, new_col) + 1);
					}
				}
			}
		}
		visited[row][col] = res;
		return res;

	}
    int maxMoves(vector<vector<int>>& grid) {
        int res = 0;
        vector<vector<int>> visited(grid.size(), vector<int>(grid[0].size(), -1));
        for (int i = 0; i < grid.size(); ++i) {
			res = max(res, helper(grid, visited, i, 0));
        }
		return res;
    }
};
