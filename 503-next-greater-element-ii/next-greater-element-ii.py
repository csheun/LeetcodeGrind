
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        # monotonic decreasing stack
        q = []
        res = [-1] * len(nums)
        # stack containing the index
        q.append(0)
        for j in range(1, len(nums) * 2 + 1):
            i = j % len(nums)
            top = nums[q[-1]]
            if nums[i] <= top:
                q.append(i)
            else:
                # clear all the elements in stack thats smaller
                while q and nums[i] > nums[q[-1]]:
                    res[q[-1]] = nums[i]
                    q.pop()
                q.append(i)
        
        return res
        
        