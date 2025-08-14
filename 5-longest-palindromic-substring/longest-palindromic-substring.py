class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force: check every substring and check for palindrome
        # dp

        if len(s) <= 1:
            return s
        max_length = 1
        max_s = s[0]

        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(i + 1):
                if (s[i] == s[j] and (i-j <= 2 or dp[j+1][i-1])):
                    dp[j][i] = True
                    if (i - j + 1 > max_length):
                        max_length = i - j + 1
                        max_s = s[j:i+1]
        return max_s
        
        