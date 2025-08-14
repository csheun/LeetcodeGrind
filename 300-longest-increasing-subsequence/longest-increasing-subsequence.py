class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        dp[i] = length of longest subsequence end with nums[i]
        need to check all indexes infront:
        if nums[x] < nums[i] then dp[i] = dp[x] + 1,
        take the maximum possible value
        ''' 

        # will minimum be 1 as it can start its own subsequence
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if (nums[j] < nums[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
        