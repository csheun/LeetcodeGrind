class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        n = row * col
        hi = n - 1
        low = 0
        
        while low <= hi:
            mid = low + (hi - low) // 2
            # convert mid to matrix index
            i = mid // col
            j = mid % col
            curr = matrix[i][j]
            if (curr == target):
                return True
            elif (curr < target):
                low = mid + 1
            else:
                hi = mid - 1
        return False
        