class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        recursion approach (TLE) + memo (pass but slow):

        compare last char of text1 and text2:
        
        if match:
            add 1 to the result of lcs on the remaining strings
            i.e. 1 + lcs(text1[:-1], text2[:-1])
        else:
            there will be 2 cases:
                last char of text1 is part of the lcs
                or last char of text2 is part of the lcs
            so 
            
            lcs = max(lcs(text1, text2[:-1]), lcs(text2, text1[:-1]))
        
        base case:
        when one of the text is empty: return 0
        '''
        # # memo[i][j] means lcs for first i char of text1 and first j char of text2
        # memo = [[-1] * (len(text1) + 1) for _ in range(len(text2) + 1)]

        # def helper(text1: str, text2: str) -> int:
        #     if memo[len(text2)][len(text1)] != -1:
        #         return memo[len(text2)][len(text1)]
        #     if not text1 or not text2:
        #         res = 0
        #     elif text1[-1] == text2[-1]:
        #         res = 1 + helper(text1[:-1], text2[:-1])
        #     else:
        #         res = max(helper(text1[:-1], text2), helper(text1, text2[:-1]))
        #     memo[len(text2)][len(text1)] = res
        #     return res
        
        # return helper(text1, text2)

        '''
        dp: subproblem stays the same , bottom up approach


        '''

        m = len(text1)
        n = len(text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # fill up initial values -> when m == 0 or n == 0 (done by above) 

        # filling up dp row by row, possible to fill up col by col as well
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[n][m]
