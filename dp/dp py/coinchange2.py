# Number of Coins

# Given a value V and array coins[] of size M, the task is to make the change for V cents, given that you have an infinite supply of each of coins{coins1, coins2, ..., coinsm} valued coins. Find the minimum number of coins to make the change. If not possible to make change then return -1.


class Solution:
    def minCoins(self, coins, M, amount):
        # chat gbt
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    # dp = [[0 for i in range(V+1)] for j in range(M+1)]
    # for i in range(1, V+1):
    #     dp[0][i] = float('inf')
    # for i in range(1, M+1):
    #     for j in range(1, V+1):
    #         if coins[i-1] > j:
    #             dp[i][j] = dp[i-1][j]
    #         else:
    #             dp[i][j] = min(dp[i][j-coins[i-1]]+1, dp[i-1][j])
    # if dp[M][V] == float('inf'):
    #     return -1
    # else:
    #     return dp[M][V]


# aditya verma method did not work
    # dp=[[0 for i in range(V+1)]for j in range(M+1)]
    # for i in range(V+1):
    #     dp[0][i]=float('inf')-1
    #     if i/coins[0]==1:
    #         dp[1][i]=1
    #     else:
    #         dp[1][i]=float('inf')-1
    # for j in range(M+1):
    #     dp[j][0]=0
    # for i in range(2,M+1):
    #     for j in range(1,V+1):
    #         if coins[i-1]<=j:
    #             dp[i][j]=min(1+dp[i][j-coins[i-1]],dp[i-1][j])
    #         else:
    #             dp[i][j]=dp[i-1][j]

    # if dp[M][V] == float('inf')-1 :
    #     return -1
    # else:
    #     return dp[M][V]
