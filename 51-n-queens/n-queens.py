class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # explore all possible position using backtracking,
        # after adding a piece, remove all positions thats not valid
        # same row, same col, diagonal


        directions = [(1, 0), (-1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

        res = []
        def backtracking(row, queen_set, remaining_set):
            queen_count = len(queen_set)
            if queen_count == n:
                res.append(queen_set)
            elif queen_count < n:
                # pick 1 in the remaining_arr to do the thing
                for i in range(n):
                    cell = (row, i)
                    if cell not in remaining_set:
                        continue
                    new_set = remaining_set.copy()
                    new_set.remove(cell)
                    for direction in directions:
                        curr = cell
                        while 0 <= curr[0] < n and 0 <= curr[1] < n:
                            next_cell = (curr[0] + direction[0], curr[1] + direction[1])
                            new_set.discard(next_cell)
                            curr = next_cell
                    backtracking(row + 1, queen_set | {cell},  new_set)
        remaining_set = set()
        for i in range(n):
            for j in range(n):
                remaining_set.add((i, j))
        
        backtracking(0, set(), remaining_set)

        res = [tuple(sorted(list(x))) for x in res]
        res = list(set(res))
        
        def convert(queen_pos):
            grid = [['.'] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if (i, j) in queen_pos:
                        grid[i][j] = 'Q'
            grid = ["".join(x) for x in grid]
            return grid
        
        res = [convert(x) for x in res]

        return res

        