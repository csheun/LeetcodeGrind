class Solution {
public:
    int uniquePaths(int m, int n) {
        std::vector<std::vector<int>> visited(m, std::vector<int>(n, -1));
        return findPath(0, 0, m, n, visited);
    }

    int findPath(int row_pos, int col_pos, int row_size, int col_size, std::vector<std::vector<int>>& visited) {
        if (visited[row_pos][col_pos] != -1) {
            return visited[row_pos][col_pos];
        }
        if (row_pos == (row_size - 1) && col_pos == (col_size - 1)) {
            visited[row_pos][col_pos] = 1;
            return 1;
        }
        int down_paths = 0;
        int right_paths = 0;
        // check if can move down and right;
        if ((row_pos + 1) < row_size) {
            down_paths = findPath(row_pos + 1, col_pos, row_size, col_size, visited);
        }
        if ((col_pos + 1) < col_size) {
            right_paths = findPath(row_pos, col_pos + 1, row_size, col_size, visited);
        }

        visited[row_pos][col_pos] = down_paths + right_paths;
        return visited[row_pos][col_pos];
    }
};