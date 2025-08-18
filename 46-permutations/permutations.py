class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(arr, remaining):
            if not remaining:
                res.append(arr)
            else:
                for i in range(len(remaining)):
                    backtrack(arr + [remaining[i]], remaining[:i] + remaining[i+1:])
        
        backtrack([], nums)

        return res
        