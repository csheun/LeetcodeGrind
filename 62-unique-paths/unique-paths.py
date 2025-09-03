class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        dp:

        unique path to reach (i, j) equals =
            unique path to reach (i - 1, j) +
            unique path to reach (i, j - 1)
        
        base cases dp(0, j) (first row) and dp(i, 0) (first col) = 1

        possible to fill up by row or col

        res at dp[m-1][n-1]

        '''
        
        dp = [[1] * n for _ in range(m)]

        # fill up row by row
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m-1][n-1]