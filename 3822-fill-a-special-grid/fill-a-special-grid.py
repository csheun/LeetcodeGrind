class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        size = 1 << n
        grid = [[0] * size for _ in range(size)]
        val = 0

        def solve(startRow, endRow, startCol, endCol):
            nonlocal val
            sz = endRow - startRow
            if sz == 1:
                grid[startRow][startCol] = val
                val += 1
                return
            midRow = startRow + sz // 2
            midCol = startCol + sz // 2

            solve(startRow, midRow, midCol, endCol) # Top right
            solve(midRow, endRow, midCol, endCol) # Bot right
            solve(midRow, endRow, startCol, midCol) # Bot left
            solve(startRow, midRow, startCol, midCol) # Top left
        
        solve(0, size, 0, size)
        return grid

        