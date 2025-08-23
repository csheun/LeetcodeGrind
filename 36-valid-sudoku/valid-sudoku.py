class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check_row() -> bool:
            for row in board:
                nums = set()
                for num in row:
                    if num != '.':
                        if num in nums:
                            return False
                        nums.add(num)
            return True

        def check_col() -> bool:
            for i in range(len(board[0])):
                nums = set()
                for j in range(len(board)):
                    num = board[j][i]
                    if num != '.':
                        if num in nums:
                            return False
                        nums.add(num)
            return True

        def check_grid() -> bool:

            directions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
            for i in range(3):
                #(i * 3)
                for j in range(3):
                #(j * 3)    
                    # print("starting pos: ")
                    # print(f"[{i*3}, [{j*3}]")
                    nums = set()
                    for direction in directions:
                        x = i * 3 + direction[0]
                        y = j * 3 + direction[1]
                        num = board[x][y]
                        if num != '.':
                            if num in nums:
                                return False
                            nums.add(num)
            return True
        
        return check_row() and check_col() and check_grid()
