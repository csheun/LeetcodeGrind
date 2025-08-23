class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n_row = len(grid)
        n_col = len(grid[0])

        queue = deque()
        
        fresh = 0
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        time = 0
        while queue:
            for i in range(len(queue)):
                x, y = queue.popleft()
                for direction in directions:
                    new_x = x + direction[0]
                    new_y = y + direction[1]
                    if 0 <= new_x < n_row and 0 <= new_y < n_col and grid[new_x][new_y] == 1:
                        fresh -= 1
                        grid[new_x][new_y] = 2
                        queue.append((new_x, new_y))
            if queue:
                time += 1
        
        return time if fresh == 0 else -1