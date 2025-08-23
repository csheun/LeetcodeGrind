class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # loop through grid, for each land do a bfs/dfs search and mark land as visited

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n_row = len(grid)
        n_col = len(grid[0])
        count = 0

        visited = [[False] * n_col for _ in range(n_row)]

        queue = deque()

        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == "1" and not visited[i][j]:
                    queue.append((i, j))
                    visited[i][j] = True
                    while queue:
                        x, y = queue.popleft()
                        # print(f"Curr_grid: {i}, {j} --- exploring: [{x},{y}]")
                        for direction in directions:
                            new_row = x + direction[0]
                            new_col = y + direction[1]
                            if 0 <= new_row < n_row and 0 <= new_col < n_col and grid[new_row][new_col] == "1" and not visited[new_row][new_col]:
                                queue.append((new_row, new_col))
                                visited[new_row][new_col] = True
                    count += 1

        return count