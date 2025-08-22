class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # first pointer on current number
        # second pointer on the next number 
        # then proceed to find a number that will make the sum == 0
        # move the second pointer to the next unqiue number and repeat
        res = []
        l_prev = None
        for i in range(len(nums) - 2):
            if l_prev is None:
                l_prev = nums[i]
            elif l_prev == nums[i]:
                continue
            r_prev = None
            j = i + 1
            k = len(nums) - 1
            while j < k and j < len(nums) -1 :
                if r_prev is not None and nums[j] == r_prev:
                    j += 1
                    continue
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    r_prev = nums[j]
                    j += 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
            l_prev = nums[i]
        
        return res
        