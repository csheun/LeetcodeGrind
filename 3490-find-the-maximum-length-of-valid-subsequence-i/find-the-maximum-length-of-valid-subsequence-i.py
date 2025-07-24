class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even_count = odd_count = 0
        alt_end_even = alt_end_odd = 0
        for num in nums:
            if (num % 2 == 0):
                # even
                even_count += 1
                alt_end_even = max(alt_end_even, alt_end_odd + 1)
            else:
                odd_count += 1
                alt_end_odd = max(alt_end_odd, alt_end_even + 1)
        return max(even_count, odd_count, alt_end_odd, alt_end_even)
        