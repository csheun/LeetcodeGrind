class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if (nums[-1] > nums[0] or len(nums) == 1):
        #     return nums[0]

        # def checkMin(nums: List[int], idx) -> bool:
        #     if idx == 0:
        #         return nums[1] > nums[idx]
        #     elif idx == len(nums) - 1:
        #         return nums[len(nums) - 2] > nums[idx]
        #     else:
        #         return nums[idx + 1] > nums[idx] and nums[idx - 1] > nums[idx]

        # # now min elem will not be the first elem so it will be between 2 elements > itself
        # lo = 0
        # hi = len(nums) - 1

        # while lo <= hi:
        #     mid = lo + (hi - lo) // 2
        #     # check left and right
        #     if checkMin(nums, mid):
        #         return nums[mid]
        #     else:
        #         # only can be left lower and right higher
        #         if nums[hi] > nums[mid]:
        #             # left side
        #             hi = mid - 1
        #         else:
        #             # right side
        #             lo = mid + 1
        # return - 1

        # A neater solution

        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if (nums[mid] > nums[hi]):
                # min element must be in between
                lo = mid + 1
            else:
                # min element will not be in between but mid element maybe the min
                hi = mid
        
        return nums[lo]
        