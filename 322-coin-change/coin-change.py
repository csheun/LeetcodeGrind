from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # bfs (works but memory exceeded)
        # if amount == 0:
        #     return 0
        # queue = deque()
        # queue.append(tuple([amount, 0]))
        # while queue:
        #     amt, cnt = queue.popleft()
        #     for coin in coins:
        #         if (amt - coin) > 0:
        #             queue.append(tuple([amt - coin, cnt + 1]))
        #         elif (amt - coin == 0):
        #             return cnt + 1
        #         # else: -ve res -> dont do anything
        # return -1 
                
        # # bfs with memoization (works)
        # if amount == 0:
        #     return 0
        # visited_amt = set()
        # visited_amt.add(amount)
        # queue = deque()
        # queue.append(tuple([amount, 0]))
        # while queue:
        #     amt, cnt = queue.popleft()
        #     for coin in coins:
        #         diff = amt - coin
        #         if diff > 0 and diff not in visited_amt:
        #             visited_amt.add(diff)
        #             queue.append(tuple([diff, cnt + 1]))
        #         elif diff == 0:
        #             return cnt + 1
        #         # else: -ve res -> dont do anything
        # return -1 

        '''
        dp solution:
        dp[i] = minimum coin change to range amount i
        '''

        if amount == 0:
            return 0
        dp = [math.inf] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if (i - coin >= 0):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != math.inf else -1
