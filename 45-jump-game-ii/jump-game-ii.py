class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_reach = 0
        curr_reach = 0
        jump_count = 0
        for i in range(len(nums)):
            if i == max_reach:
                jump_count += 1
                max_reach = max(curr_reach, i + nums[i])
                if (max_reach >= len(nums) - 1):
                    break
                curr_reach = max_reach
            else:
                curr_reach = max(curr_reach, i + nums[i])
        
        return jump_count
            