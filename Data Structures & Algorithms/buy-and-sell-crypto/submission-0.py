class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # window with largest positive difference

        # [7,1,5,3,6,4]
        buy = 0
        max_profit = 0
        for sell in range(1, len(prices)):
            while prices[sell] - prices[buy] < 0 and buy < sell:
                buy += 1
            
            if prices[sell] - prices[buy] > max_profit:
                max_profit = max(max_profit,prices[sell] - prices[buy])

        return max_profit 

