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

        '''
        Binary search (recommended way)
        '''
        res_arr = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > res_arr[-1]:
                res_arr.append(nums[i])
            elif nums[i] < res_arr[-1]:
                # find the smallest number that is bigger than it to replace
                idx = bisect_left(sub, nums[i])
                sub[idx] = nums[i]
        
        return len(res_arr)
            