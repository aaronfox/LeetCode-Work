# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # Brute force solution (TLE)
        # # O(n^2) time complexity
        # # O(1) space complexity
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         if prices[j] - prices[i] > max_profit:
        #             max_profit = prices[j] - prices[i]
        
                # The idea here is to continually iterate and find the lowest price.
        # Then, if the current price minus the lowest price is higher than the current highest price,
        # set the highest_price is set to the current price minus the lowest price
        # O(n) runtime complexity
        # O(1) space complexity
        lowest_price = math.inf
        max_profit = 0

        for price in prices:
            lowest_price = min(lowest_price, price)
            max_profit = max(max_profit, price - lowest_price)
            
        return max_profit
