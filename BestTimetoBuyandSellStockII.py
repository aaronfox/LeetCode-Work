# Problem URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Because Python doesn't like recursion for the brute force approach
import sys
sys.setrecursionlimit(10000)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force approach that is O(n^n)
        # return self.recursive_calculate(prices, 0)
        
        # One Pass Peak Valley-like approach
        return self.peak_valley(prices)
    
    # O(n) runtime and O(1) space used
    def peak_valley(self, prices):
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxprofit = maxprofit + prices[i] - prices[i-1]
                
                
        return maxprofit
    
    
    
    # Unfinished Python friendly version of the recursive solution
#     def iterative_calculate(self, prices, s):
#         stack = []
#         stack.push([prices, 0])
        
#         max = 0
#         while len(stack) > 0:
#             curr_obj = stack.pop()
            
#             if curr_obj[1] >= len(prices):
#                 pass
#             for start in range(curr_obj[1], len(curr_obj[0])):
#                 maxprofit = 0
#                 for i in range(start + 1, len(curr_obj[0])):
#                     if curr_obj[0][start] < curr_obj[0][i]:
#                         profit = prices[i] - prices[start]
#                         if profit > maxprofit:
#                             maxprofit = profit
                            
#                 if maxprofit > max:
#                     max = maxprofit
                    
#         return max
                
        
#         # Recursive base case
#         if s >= len(prices):
#             return 0
#         max = 0
#         for start in range(s, len(prices)):
#             maxprofit = 0
#             for i in range(start + 1, len(prices)):
#                 if prices[start] < prices[i]:
#                     profit = self.recursive_calculate(prices, i + 1) + prices[i] - prices[start]
#                     if profit > maxprofit:
#                         maxprofit = profit
            
#             if maxprofit > max:
#                 max = maxprofit
        
#         return max
        
    # Recursive solution that caps out in Python because Python does not handle recursion well 
    def recursive_calculate(self, prices, s):
        # Recursive base case
        if s >= len(prices):
            return 0
        max = 0
        for start in range(s, len(prices)):
            maxprofit = 0
            for i in range(start + 1, len(prices)):
                if prices[start] < prices[i]:
                    profit = self.recursive_calculate(prices, i + 1) + prices[i] - prices[start]
                    if profit > maxprofit:
                        maxprofit = profit
            
            if maxprofit > max:
                max = maxprofit
        
        return max
        
        