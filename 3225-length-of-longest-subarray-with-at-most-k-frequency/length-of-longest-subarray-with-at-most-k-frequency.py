from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # every element in the subarry has freq <= k
        freq = defaultdict(int)
        res = 0
        l = 0
        r = 0
        while r < len(nums):
            freq[nums[r]] += 1
            if freq[nums[r]] > k:
                # move the left pointer till it removes the same element
                while nums[l] != nums[r]:
                    freq[nums[l]] -= 1
                    l += 1
                l += 1
                freq[nums[r]] = k
            res = max(res, r -  l + 1)
            r += 1
        return res

        