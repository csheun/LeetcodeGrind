class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_dict = {}
        prefix_sum_dict[0] = 1
        total = 0
        count = 0
        for i in range(len(nums)):
            total += nums[i]
            if (total - k in prefix_sum_dict):
                count += prefix_sum_dict[total - k]
            if total not in prefix_sum_dict:
                prefix_sum_dict[total] = 0
            prefix_sum_dict[total] += 1
        return count