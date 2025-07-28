class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_value = 0
        for num in nums:
            max_value |= num
        
        def subsets(nums):
            res = []

            def backtrack(start, path):
                if path:  # Only add non-empty subsets
                    res.append(path[:])
                for i in range(start, len(nums)):
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()

            backtrack(0, [])
            return res
        working_set = subsets(nums)
        count = 0
        for subset in working_set:
            result = 0
            for num in subset:
                result |= num
            if (result == max_value):
                count += 1
        return count
                