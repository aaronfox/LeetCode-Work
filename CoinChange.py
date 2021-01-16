# URL: https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dynamic Programming approach
        
        # DP assumes an array with all solutions of minimum coins up to amount
        # O(n*c) runtime complexity where n is the size of amount and c is the number of coins
        # O(n) space complexity where n is the size of amount
        if amount < 1:
            return 0
        dp = [0] * (amount + 1)
        
        for sum in range(1, amount + 1):
            min = -1
            for coin in coins:
                # Check if coin is usable still and if the combo hasn't already been determined unusable
                if sum >= coin and dp[sum - coin] != -1:
                    curr = dp[sum - coin] + 1
                    if min < 0 or curr < min:
                        min = curr
                        
            dp[sum] = min
        return dp[amount]
        
        
        
        # Recursive solution for finding min coins
        # Takes O(n) space where n == amount
        # Takes C^n time complexity, where c is the number of coins and n is the amount
        count = 0
        if amount == 0:
            return 0
        else:
            curr_coins = [0] * amount
            return self.recursiveCoin(coins, amount, curr_coins)
        
    def recursiveCoin(self, coins, amount_left, curr_coins):
        # Base cases
        if amount_left < 0:
            return -1
        if amount_left == 0:
            return 0
        if curr_coins[amount_left - 1] != 0:
            return curr_coins[amount_left-1]
        min = math.inf
        for coin in coins:
            curr = self.recursiveCoin(coins, amount_left - coin, curr_coins)
            if curr >= 0 and curr < min:
                min = curr + 1
                
        if min == math.inf:
            curr_coins[amount_left - 1] = -1
        else:
            curr_coins[amount_left - 1] = min
        
        return curr_coins[amount_left - 1] 
        
        
        # Greedy approach: doesn't work for all coin denominations unfortunately
        # E.g. it doesn't work for [9, 6, 5, 1] since greedy will return 9, 1, 1 instead of 6, 5
#         curr_amount = 0
#         num_coins = 0
#         # Must sort list of coins
#         coins.sort()
#         while curr_amount != amount:
#             found_coin = False
#             for i in range(len(coins) - 1, -1, -1):
#                 if coins[i] <= amount - curr_amount:
#                     curr_amount += coins[i]
#                     num_coins += 1
#                     found_coin = True
#                     break
#             if found_coin == False:
#                 return -1
                    
#         return num_coins 
