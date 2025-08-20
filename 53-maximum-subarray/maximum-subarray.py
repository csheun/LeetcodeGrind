class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # when is -ve then i start new as it is always good to have accumulated somthing 
        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            if (curr_sum < 0):
                curr_sum = 0
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
        return max_sum 
            
            
        