class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # # intuition is to do backtracking with memo (works but TLE at larger input testcases)

        # visited = {}

        # def dfs(idx: int, total_sum: int):
        #     key = tuple(list[idx, total_sum])
        #     if key in visited:
        #         return visited[key]
        #     if total_sum == amount:
        #         visited[key] = 1
        #         return 1
        #     elif total_sum > amount:
        #         visited[key] = 0
        #         return 0
        #     else:
        #         # total_sum < amount
        #         res = 0
        #         for i in range(idx, len(coins)):
        #              res += dfs(i, total_sum + coins[i])
        #         visited[key] = res
        #         return res
        # return dfs(0, 0)

        # dp: loop through the numbers and add to the dp 

        dp = [0] * (amount + 1)

        dp[0] = 1

        for i in range(len(coins)):
            for j in range(len(dp)):
                if dp[j]:
                    if j + coins[i] < len(dp):
                        dp[j + coins[i]] += dp[j]
        return dp[amount]
        

