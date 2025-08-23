class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(start, path):
            res.append(path)
            for i in range(start + 1, len(nums)):
                if i == start + 1:
                    backtrack(i, path + [nums[i]])
                if i > start + 1 and nums[i] != nums[i - 1]:
                    backtrack(i, path + [nums[i]])
        backtrack(-1, [])

        return res
        