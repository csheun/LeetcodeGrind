class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        count = 0

        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            # dp[i][i] = True
            # count += 1
            for j in range(i + 1):
                if (s[j] == s[i] and (i - j <= 2 or dp[j+1][i-1])):
                    dp[j][i] = True
                    count += 1
        
        return count
        