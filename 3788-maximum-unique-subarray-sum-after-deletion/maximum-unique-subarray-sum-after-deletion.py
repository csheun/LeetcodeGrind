class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        pos_flag = False
        for num in nums:
            if num > 0:
                res += num
                pos_flag = True
        if not pos_flag:
            return max(nums)
        return res
        