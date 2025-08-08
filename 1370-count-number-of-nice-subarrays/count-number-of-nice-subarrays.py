class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [0 if x % 2 == 0 else 1 for x in nums]
        sub_arr_map = {0:1}
        total = count = 0
        for num in nums:
            total += num
            if (total - k in sub_arr_map):
                count += sub_arr_map[total - k]
            sub_arr_map[total] = sub_arr_map.get(total, 0) + 1
        return count