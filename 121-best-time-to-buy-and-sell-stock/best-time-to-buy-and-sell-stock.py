class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = max_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            price = prices[i]
            if price < min_price:
                min_price = price
                max_price = price
            elif price > max_price:
                max_price = price
                profit = max_price - min_price
                max_profit = max(max_profit, profit)
        return max_profit
            

    
        