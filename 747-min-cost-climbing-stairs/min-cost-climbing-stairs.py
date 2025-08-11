class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # min cost of getting to ith step is = min ((i - 1)th step + cost[i - 1] , (i - 2)th step + cost[i -2])
        prev = curr = 0
        for i in range(2, len(cost) + 1):
            temp = min(prev + cost[i - 2], curr + cost[i - 1])
            prev = curr
            curr = temp
        return curr

        