class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # look at each cell, if found 'O' do BFS to find neighbour 'O's
        # mark visited to avoid repeating
        # save the list -> have a flag to check if theres any on the edge
        # if dont have the loop through the list and mark all as 'X'

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n_row = len(board)
        n_col = len(board[0])

        for i in range(n_row):
            for j in range(n_col):
                visited = set()
                if board[i][j] == 'O' and (n_row, n_col) not in visited:
                    region = []
                    queue = deque()
                    queue.append((i, j))
                    visited.add((i, j))
                    edge = False
                    while queue:
                        x, y = queue.popleft()
                        if x == 0 or x == n_row - 1 or y == 0 or y == n_col - 1:
                            edge = True
                        region.append((x,y))
                        for direction in directions:
                            new_x = x + direction[0]
                            new_y = y + direction[1]
                            if 0 <= new_x < n_row and 0 <= new_y < n_col:
                                if board[new_x][new_y] == 'O' and (new_x, new_y) not in visited:
                                    queue.append((new_x, new_y))
                                    visited.add((new_x, new_y))
                    if not edge:
                        for pos in region:
                            board[pos[0]][pos[1]] = 'X'
            


        