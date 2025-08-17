class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if (nums[mid] == target):
                return mid
            # if nums[hi] > nums[mid]: this subarray must be increasing

            # case 1: target > nums[mid] and target <= nums[hi]
            # ie. [... ,(mid)7, 8, 9, 10, (hi)11], target = 8
            # case 2: target > nums[mid] and nums[mid] > nums[hi]
            # ie. [... ,(mid)7, 8, 0, 1, (hi)4], target = 8
            # case 3: nums[mid] > nums[hi] and target <= nums[hi]
            # ie. [... ,(mid)7, 8, 0, 1, (hi)4], target = 3

            elif (target > nums[mid] and target <= nums[hi]) or (target > nums[mid] and nums[mid] > nums[hi]) or (nums[mid] > nums[hi] and target <= nums[hi]):
                lo = mid + 1
            else:
                hi = mid - 1

        return -1