class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = 0
        curr_score = 0

        left_ptr = 0
        right_ptr = 0

        sub_arr_hash = {}

        while (right_ptr < len(nums)):
            curr = nums[right_ptr]
            if (curr in sub_arr_hash):
                next_idx = sub_arr_hash[curr] + 1
                while (left_ptr < next_idx):
                    ## minus score from curr_score
                    ## remove element from hash
                    curr_score -= nums[left_ptr]
                    del sub_arr_hash[nums[left_ptr]]
                    left_ptr += 1
            sub_arr_hash[curr] = right_ptr
            curr_score += curr
            max_score = max(max_score, curr_score)
            right_ptr += 1

        return max_score

        