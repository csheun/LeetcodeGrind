class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        res = []

        def backtrack(idx, count, arr):
            if count == 3:
                value = (arr[0] - arr[1]) * arr[2]
                res.append(value)
            else:
                for i in range(idx + 1, len(nums)):
                    backtrack(i, count + 1, arr + [nums[i]])
        
        backtrack(-1, 0, [])

        val = max(res)
        return max(0, val)

        