class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # find wheres the starting sq and ending sq and the number of empty squares
        m, n = len(grid), len(grid[0])
        start = end = None
        required_sq = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    required_sq += 1
                elif grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
        
        def backtrack(i, j, path):
            if (i, j) == end and len(path) == required_sq:
                return 1
            if (i , j) == end and len(path) != required_sq:
                return 0
            if len(path) == required_sq and (i, j) != end:
                return 0
            res = 0
            for direction in directions:
                row = i + direction[0]
                col = j + direction[1]
                if 0 <= row < m and 0 <= col < n:
                    if (row, col) not in path and grid[row][col] != -1:
                        res += backtrack(row, col, path | {(row, col)})
            return res
        
        return backtrack(start[0], start[1], {start})

        