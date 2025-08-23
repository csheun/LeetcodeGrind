class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # two-pointer / sliding window
        # expand window when product < k
        # shrink window when product >= k
        # when window expanded, additional subarry count is (right - left + 1) 
        # new subarry introduced is [right], [right -1, right] ... [left, right]
        # so there is (right - left + 1) of these

        l = 0
        product = 1
        count = 0
        for r in range(len(nums)):
            product *= nums[r]
            if product >= k:
                # shrink left side
                while product >= k and l <= r:
                    product /= nums[l]
                    l += 1
            count += r - l + 1
        return count
                
        