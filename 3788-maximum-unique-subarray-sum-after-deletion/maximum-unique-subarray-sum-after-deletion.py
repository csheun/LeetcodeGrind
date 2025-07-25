class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        least_nvg = float(-inf)
        count = 0
        for num in nums:
            if num > 0:
                res += num
                count += 1
            else:
                least_nvg = max(least_nvg, num)
        if count == 0:
            return least_nvg
        return res
        