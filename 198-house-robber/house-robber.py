class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[n] = max(dp[n - 2] + nums[n], dp[n - 1])
        if (len(nums) == 1):
            return nums[0]
        # more than 2
        minus_2 = nums[0]
        minus_1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr = max(minus_2 + nums[i], minus_1)
            minus_2 = minus_1
            minus_1 = curr
        return minus_1
        