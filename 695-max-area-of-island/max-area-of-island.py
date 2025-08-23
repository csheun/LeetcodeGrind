class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        n_row = len(grid)
        n_col = len(grid[0])
        queue = deque()
        res = 0
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j]:
                    queue.append((i,j))
                    grid[i][j] = 0
                    count = 0
                    while queue:
                        x, y = queue.popleft()
                        count += 1
                        for direction in directions:
                            new_row = x + direction[0]
                            new_col = y + direction[1]
                            if 0 <= new_row < n_row and 0 <= new_col < n_col and grid[new_row][new_col]:
                                queue.append((new_row, new_col))
                                grid[new_row][new_col] = 0

                    res = max(res, count)
        return res