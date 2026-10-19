class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        # greedy: start buying from the largest
        # counting sort
        freq = [0] * max(cost)
        for c in cost:
            freq[c - 1] += 1
        # form array
        cost_sorted = []
        for i in range(len(freq)):
            tmp = [i + 1] * freq[i]
            cost_sorted.extend(tmp)
        res = 0
        count = 1
        print(cost_sorted)
        for i in range(len(cost_sorted)-1, -1, -1):
            if count == 1 or count == 2:
                res += cost_sorted[i]
                count += 1
            else:
                count = 1
        return res
        