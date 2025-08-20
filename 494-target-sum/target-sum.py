class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # # recursive DFS style (TLE)
        # res = [0]
        # def helper(idx: int, total_sum: int):
        #     if idx == len(nums) -1:
        #         if total_sum == target:
        #             res[0] += 1
        #     else:
        #         helper(idx + 1, total_sum + nums[idx + 1])
        #         helper(idx + 1, total_sum - nums[idx + 1])
        
        # helper(-1, 0)

        # return res[0]

        # DP:

        # limit = sum(nums)
        # dp = [False] * (2 * limit + 1)
        # dp[limit] = True
        # for i in range(len(nums)):
        #     if (i == len(nums) - 1):
        #         # last one
        #         # check target - num or target + num is True
        #         if dp[target - num + limit] 
        #     num = nums[i]
        #     for i in range(len(dp)):
        #         if dp[i]:
        #             dp[i - num] = True
        #             dp[i + num] = True
        
        values = [0]
        for i in range(len(nums)):
            num = nums[i]
            curr_values = []
            for value in values:
                curr_values.append(value - num)
                curr_values.append(value + num)
            values = curr_values
        
        count = 0
        for value in values:
            if value == target:
                count += 1
        
        return count