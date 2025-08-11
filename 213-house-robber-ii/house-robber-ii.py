class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # compute twice rob day 1 and not rob day 1 -> then get max
        

        # case 1 -> rob day 1
        # dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        minus2 = nums[0]
        minus1 = nums[0]
        for i in range(2, len(nums) - 1):
            curr = max(minus2 + nums[i], minus1)
            minus2 = minus1
            minus1 = curr
        val_1 = minus1

        minus2 = 0
        minus1 = nums[1]
        for i in range(2, len(nums)):
            curr = max(minus2 + nums[i], minus1)
            minus2 = minus1
            minus1 = curr
        val_2 = minus1

        return max(val_1, val_2)