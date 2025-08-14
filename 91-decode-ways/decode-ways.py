class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        1) recursion - look at the first digit if can then check the
        remaining string + look at the first 2 digit (TIME LIMIT EXCEEDED)
        '''
        # if not s:
        #     return 1
        # if (int(s[0]) == 0):
        #     return 0
        # if (len(s) == 1):
        #     return 1
        # if (int(s[0:2]) <= 26):
        #     return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        # else:
        #     return self.numDecodings(s[1:])
        '''
        2) Dp (break into subproblem)

        dp[i] += dp[i - 1] if s[i] != 0
        dp[i] += dp[i - 1] if s[i-1:i+1] >= 10 <=26
        '''
        # dp tracks the ways to decode message[:idx]
        # ie dp[2] = ways to decode messages of length 2 -> msg[0:2]
        # ie dp[n] = ways to msgs of length n thefore len(dp) = n + 1

        # if int(s[0]) == 0:
        #     return 0
        
        # dp = [0] * (len(s) + 1)

        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2, len(s) + 1):
        #     digit_1 = int(s[i - 1])
        #     digit_2 = int(s[i-2:i])

        #     if (digit_1 != 0):
        #         dp[i] += dp[i - 1]
        #     if (digit_2 >= 10 and digit_2 <= 26):
        #         dp[i] += dp[i - 2]
            
        # return dp[len(s)]
        
        '''
        3) Optimise space -> use 2 variables to keep track
        '''

        if int(s[0]) == 0:
            return 0

        prev = 1
        curr = 1
        for i in range(2, len(s) + 1):
            digit_1 = int(s[i - 1])
            digit_2 = int(s[i-2:i])
            temp = 0
            if (digit_1 != 0):
                temp += curr
            if (digit_2 >= 10 and digit_2 <= 26):
                temp += prev
            prev = curr
            curr = temp
        return curr