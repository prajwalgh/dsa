val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

# this is recursice approach              error : Time Limit Exceeded


def knapSack(W, wt, val, n):
    # base case
    if W == 0 or n == 0:
        return 0
    # main body
    if wt[n - 1] <= W:
        return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1), knapSack(W, wt, val, n - 1))
    elif wt[n - 1] > W:
        # print(val[n-1])
        return knapSack(W, wt, val, n - 1)


print(knapSack(W, wt, val, n))

# memoization approach -----------------------------------

# method 1


class Solution:

    # Function to return max value that can be put in knapsack of capacity W.

    def __init__(self):
        self.memo = [[-1 for i in range(1001)] for j in range(1001)]

    def knapSack(self, W, wt, val, n):
        if n == 0 or W == 0:
            return 0
        if self.memo[n][W] != -1:
            return self.memo[n][W]
        if wt[n-1] <= W:
            self.memo[n][W] = max(
                val[n-1]+self.knapSack(W-wt[n-1], wt, val, n-1), self.knapSack(W, wt, val, n-1))
            return self.memo[n][W]
        elif wt[n-1] > W:
            self.memo[n][W] = self.knapSack(W, wt, val, n-1)
            return self.memo[n][W]
# memoization approach -----------------------------------
# dp solution ...........................
# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W

# method 2


def knapSack_memo(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                              + K[i - 1][w - wt[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


print(knapSack_memo(W, wt, val, n))
