class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # loop through the board to find the first char of str
        # try to form the word -> backtracking to explore different paths
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def backtrack(grid_row, grid_col, nxt_idx, visited):
            # print(f"row: {grid_row}, col: {grid_col}, nxt_idx: {nxt_idx}, visited: {visited}")
            if nxt_idx == len(word):
                return True
            # different directions
            res = False
            for direction in directions:
                row = grid_row + direction[0]
                col = grid_col + direction[1]
                if row >= 0 and row < n_row and col >= 0 and col < n_col and tuple([row, col]) not in visited and board[row][col] == word[nxt_idx]:
                    # change visited from array to set to improve look up time
                    entry = tuple([row, col])
                    res = res or backtrack(row, col, nxt_idx + 1, visited + [entry])
                    
            return res
        
        n_row = len(board)
        n_col = len(board[0])

        for i in range(n_row):
            for j in range(n_col):
                grid = board[i][j]
                if grid == word[0]:
                    if len(word) == 1:
                        return True
                    # start search
                    result = backtrack(i, j, 1, [tuple([i, j])])
                    if result:
                        return result
        
        return False