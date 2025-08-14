class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # sum up 
        total = sum(nums)
        if (total % 2 != 0):
            return False
        target = int(total / 2)

        # goal: check if there is a subset of nums that can sum up to this
        # dp[i] = True when it is possible to get a sum of i
        n = len(nums)
        dp = [False] * (target + 1)
        dp[0] = True

        # intuition: loop through each number and see which sum can be created so far
        # i.e [1, 5, 11]
        # first loop: 1, dp[1] = True
        # second loop: 5, dp[5], dp[6] = True
        # third loop: 11, dp[12], dp[16], dp[17] = True
        # build until if target sum = true

        # cannot build forward as number may be reused.
        # i.e first loop 3: dp[3] = true
        # then check dp[3] == true -> yes then wrongly set dp[6] = true as well
        # number 3 is reused

        #check backwards

        for num in nums:
            for i in range(len(dp) - 1, num - 1, -1):
                if dp[i]:
                    continue
                if dp[i - num]:
                    dp[i] = True
                if dp[-1]:
                    return True
        return False