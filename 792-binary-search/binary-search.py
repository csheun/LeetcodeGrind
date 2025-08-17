class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hi = len(nums) - 1
        low = 0
        while low <= hi:
            # print(f"low: {low}, hi: {hi}")
            mid = low + (hi - low) // 2
            # print(f"mid: {mid}, elem: {nums[mid]}")
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                # search in the left half
                hi = mid - 1
            else:
                low = mid + 1
        return -1
        