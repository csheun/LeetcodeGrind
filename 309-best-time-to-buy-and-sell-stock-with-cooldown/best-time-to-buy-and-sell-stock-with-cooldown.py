class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        naive approach to find all possible
        backtracking with memo (Memory Limit Exceed)

        buy, sell, wait, cd

        '''

        # memo = {}

        # def backtrack(day, profit, on_cooldown, buy_price):
        #     if (day, profit, on_cooldown, buy_price) in memo:
        #         return memo[(day, profit, on_cooldown, buy_price)]
        #     if day == len(prices):
        #         memo[(day, profit, on_cooldown, buy_price)] = profit
        #         return profit
        #     res = []
        #     # buy
        #     if buy_price == -1 and not on_cooldown:
        #         res.append(backtrack(day + 1, profit, False, prices[day]))
        #     # sell
        #     if buy_price != -1:
        #         new_profit = profit + prices[day] - buy_price
        #         res.append(backtrack(day + 1, new_profit, True, -1))
        #     # dont do anything and wait 
        #     res.append(backtrack(day + 1, profit, False, buy_price))
        #     memo[(day, profit, on_cooldown, buy_price)] = max(res)
        #     return max(res)

        # return backtrack(0, 0, False, -1)

        '''
        dp: keep track of 3 states(s0: can buy, s1: can sell, s2:take a rest (cd))

        s0[i] = max(s0[i - 1], s2[i - 1]) -> do nothing from prev day or rested from s2
        s1[i] = max(s0[i - 1] - prices[i], s1[i - 1]) -> do nothing from prev day or buy today
        s2[i] = s1[i - 1] + prices[i]

        base case:
        s0[0] = 0 no profit at start
        s1[0] = -prices[0]
        s2[0] = 0

        '''

        n = len(prices)
        s0, s1, s2 = [[0] * n for _ in range(3)]

        s1[0] = -prices[0]

        for i in range(1, len(prices)):
            s0[i] = max(s0[i - 1], s2[i - 1])
            s1[i] = max(s1[i - 1], s0[i - 1] - prices[i])
            s2[i] = s1[i - 1] + prices[i]
        
        return max(s0[n - 1], s1[n - 1], s2[n - 1])
            
        