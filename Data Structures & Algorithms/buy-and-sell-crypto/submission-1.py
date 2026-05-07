class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force:
        # try every two pairs by looping through i then through j

        # optimal:
        # start with day 0 and 1, if there is no profit, try next window
        # once profit is reached, keep expanding window to try and get a 
        # higher profit
        # shorten window once there's no profit again
        # each element is seen at most 2 times, so time is O(n) and space is O(1)


        # [10,1,5,6,7,1]
        buy = 0
        max_profit = 0
        
        for sell in range(1, len(prices)):
            while prices[sell] - prices[buy] < 0:
                buy += 1

            max_profit = max(max_profit, prices[sell] - prices[buy])

        return max_profit
            
