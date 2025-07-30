class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        curr_and = nums[0]
        max_and = 1
        curr_count = 0

        for num in nums:
            if (curr_and & num < curr_and or curr_and & num < num):
                # bitwise & num -> drop in value
                # register prev value
                if (curr_and > max_and):
                    res = curr_count
                    max_and = curr_and
                elif (curr_and == max_and):
                    res = max(res, curr_count)
                # reset values
                curr_count = 0
                curr_and = num                
            curr_count += 1
            curr_and &= num
        
        if (curr_and > max_and):
            res = curr_count
            max_and = curr_and
        elif (curr_and == max_and):
            res = max(res, curr_count)

        return res
                
        