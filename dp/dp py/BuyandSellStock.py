# 21. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
class Solution(object):
    def maxProfit(self, prices):
        miniT = prices[0]
        maxT = 0
        for i in range(len(prices)):
            miniT = min(miniT, prices[i])
            profT = prices[i]-miniT
            maxT = max(profT, maxT)
        return maxT


# 122. Best Time to Buy and Sell Stock II

# Share
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and / or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.
class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit = profit+(prices[i]-prices[i-1])
        return profit


# 123. Best Time to Buy and Sell Stock III
# Hard

# 6903

# 136

# Add to List

# Share
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete at most two transactions.

# Note: You may not engage in multiple transactions simultaneously(i.e., you must sell the stock before you buy again).


# Example 1:

# Input: prices = [3, 3, 5, 0, 0, 3, 1, 4]
# Output: 6
# Explanation: Buy on day 4 (price=0) and sell on day 6 (price=3), profit = 3-0 = 3.
# Then buy on day 7 (price=1) and sell on day 8 (price=4), profit = 4-1 = 3.
