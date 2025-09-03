class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        dp: similiar to unique path 1 except that if cell has obstacle dont add it

        dp[i][j] = dp[i-1][j] + dp[i][j-1] if grid is not an obstacle
        '''
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        # base cases
        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        
        # first row
        for i in range(1, n):
            if obstacleGrid[0][i]:
                dp[0][i] = 0
            else:
                dp[0][i] = dp[0][i - 1]


        # first col
        for i in range(1, m):
            if obstacleGrid[i][0]:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i - 1][0]

        # fill up bottom up, row wise
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


        