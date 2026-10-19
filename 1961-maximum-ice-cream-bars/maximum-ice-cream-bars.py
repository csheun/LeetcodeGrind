class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        # counting sort
        count_freq = [0] * (10 ** 5)
        for cost in costs:
            count_freq[cost - 1] += 1
        sorted_costs = []
        for i in range(len(count_freq)):
            if count_freq[i] != 0:
                tmp = [i + 1] * count_freq[i]
                sorted_costs.extend(tmp)
        print(sorted_costs)
        # greedy: take all min
        res = 0
        for cost in sorted_costs:
            if cost <= coins:
                res += 1
                coins -= cost
            else:
                break
        return res

            
        