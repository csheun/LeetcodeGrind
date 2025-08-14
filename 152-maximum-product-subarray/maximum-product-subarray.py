class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # # brute force: loop through all position subarray and calc product (TLE)
        # if len(nums) == 1:
        #     return nums[0]
        # max_prod = nums[0] * nums[1]
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         prod = 1
        #         for k in range(i, j + 1):
        #             prod *= nums[k]
        #         if (prod > max_prod):
        #             max_prod = prod
        
        # return max_prod
        
        # dp: track max and min product value at each element
        # the max product value for next element maybe -ve * min_product value

        # general thoughts: here dont really have to consider subarray as 
        # multiplication itself is different from addition, the absolute value
        # will keep always get larger and larger (unless hit 0)
    
        res = nums[0]
        curr_max = curr_min = 1
        for num in nums:
            # num may be -ve or need to keep track of curr_min as well
            # num itself maybe the largest
            val = (num, num * curr_max, num * curr_min)
            curr_max = max(val)
            curr_min = min(val)
            res = max(res, curr_max)
        return res