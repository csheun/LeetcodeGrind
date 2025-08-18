class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        def helper(idx, total_sum, arr):
            if total_sum == target:
                res.append(arr)
            elif total_sum < target:
                for i in range(idx, len(candidates)):
                    if i > idx and candidates[i] == candidates[i-1]:
                        continue
                    curr_sum = total_sum + candidates[i]
                    helper(i + 1, curr_sum, arr + [candidates[i]])
        
        res = []
        helper(0, 0, [])
        return res
        