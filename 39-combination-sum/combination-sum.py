class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(idx: int, total_sum: int, arr: List[int]):
            if (total_sum == target):
                res.append(arr)
            elif (total_sum < target):
                # avoided duplicates by 
                for i in range(idx, len(candidates)):
                    new_sum = total_sum + candidates[i]
                    helper(i, new_sum, arr + [candidates[i]])
        res = []
        helper(0, 0, [])
        return res
        