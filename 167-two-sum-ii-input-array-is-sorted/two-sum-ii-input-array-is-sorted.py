class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            c_sum = numbers[l] + numbers[r]
            if c_sum == target:
                break
            elif c_sum  > target:
                r -= 1
            else:
                l += 1
        
        return [l + 1, r + 1]
        