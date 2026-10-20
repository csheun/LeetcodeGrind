class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i == sum([int(x) for x in list((str(num)))]):
                return i
        return -1
        