class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        State: dp[i][j] = min operations to convert s1[:i] → s2[:j]

        convert first i letters of s1 to first j letters of s2




        3 actions:
            1) delete
            dp[i][j] = 1 + dp[i-1][j]
            becos dp[i-1][j] has already converted text1 to text2, having i is not necessary so need to delete
            2) insert
            dp[i][j] = 1 + dp[i][j-1]
            with i letters, i can form j-1 text2 now there is a new letter j, i have to insert it 
            3) replace
            # if the last letter of the 2 words differ then we need to replace
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] 
            else:
                dp[i][j] = 1 + dp[i-1][j-1]      
        '''

        m = len(word1)
        n = len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # setting up base cases

        # min cost for converting 0 letter of s1 to first j letter of s2 is j
        for j in range(n + 1):
            dp[0][j] = j
        
        # min cost for converting i letters of s1 to 0 letter of s2 is i
        for i in range(m + 1):
            dp[i][0] = i

        # fill up row wise

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(
                    dp[i-1][j] + 1,
                    dp[i][j-1] + 1,
                    dp[i-1][j-1] if word1[i - 1] == word2[j - 1] else dp[i-1][j-1] + 1  
                )
        
        return dp[m][n]
        




        