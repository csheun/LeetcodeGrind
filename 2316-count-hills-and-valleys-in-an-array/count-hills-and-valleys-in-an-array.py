class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        i = 1
        while (i < len(nums)):
            if (nums[i - 1] > nums[i]):
                while (i + 1 < len(nums)):
                    if (nums[i + 1] > nums[i]):
                        # vally found
                        count += 1
                        break
                    elif (nums[i + 1] ==  nums[i]):
                        i += 1
                        continue
                    else:
                        break
            elif (nums[i - 1] < nums[i]):
                while (i + 1 < len(nums)):
                    if (nums[i + 1] < nums[i]):
                        # hill found
                        count += 1
                        break
                    elif (nums[i + 1] ==  nums[i]):
                        i += 1
                        continue
                    else:
                        break
            i += 1
        return count