class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if (i > max_reach):
                return False
            max_reach = max(i + nums[i], max_reach)
            if max_reach >= len(nums):
                return True
        return True
        