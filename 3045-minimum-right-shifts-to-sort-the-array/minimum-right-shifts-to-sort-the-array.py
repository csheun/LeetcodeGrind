class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        # it will be possible
        isSorted = True
        res_idx = -1

        for i in range(1, len(nums)):
            if not isSorted:
                if nums[i] > nums[0] or nums[i] < nums[i - 1]:
                    return -1
            else:
                if nums[i] < nums[i - 1]:
                    isSorted = False
                    res_idx = i
        
        if isSorted:
            return 0
            
        if nums[res_idx] < nums[0]:
            return len(nums) - res_idx
        else:
            return -1 
        