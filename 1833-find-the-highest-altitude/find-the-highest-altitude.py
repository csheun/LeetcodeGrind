class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        max_sum = 0
        sum = 0
        for i in range(len(gain)):
            sum += gain[i]
            max_sum = max(sum, max_sum)
        
        return max_sum
        