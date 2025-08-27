class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = set()

        for i in range(len(nums)):
            if nums[i] == key:
                for j in range(-k, k + 1):
                    idx = i + j
                    if 0 <= idx < len(nums):
                        res.add(idx)
        
        return sorted(list(res))
        