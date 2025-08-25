class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        def process(nums: List[int]) -> (int, int):
            # return sum and number of zeros
            total = 0
            zero_count = 0
            for num in nums:
                if num == 0:
                    zero_count += 1
                total += num
            return total, zero_count

        total1, zero_count1 = process(nums1)
        print(f"total: {total1}, count: {zero_count1}")
        total2, zero_count2 = process(nums2)
        print(f"total: {total2}, count: {zero_count2}")
        smaller_zero_count = zero_count1 if total1 <= total2 else zero_count2
        larger_zero_count = zero_count1 if total1 > total2 else zero_count2

        if abs(total1 - total2):
            # theres a difference, then the smaller num cannot have no zero_count
            if smaller_zero_count == 0:
                return -1
            if not larger_zero_count and min(total1, total2) + smaller_zero_count > max(total1, total2):
                return -1

        if abs(total1 - total2) == 0:
            # if theres no difference, then cannot be 1 have zero_count and 1 dont have zero_count
            if (zero_count1 and not zero_count2):
                return -1
            elif (zero_count2 and not zero_count1):
                return -1
        
        return max(total1 + zero_count1, total2 + zero_count2)

        