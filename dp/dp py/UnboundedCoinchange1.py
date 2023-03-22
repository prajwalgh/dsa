class Solution:
    def count(self, coins, N, sum1):
        dp = [[0 for i in range(sum1+1)]for j in range(N+1)]
        dp[0][0] = 1
        for i in range(1, N+1):
            for j in range(sum1+1):
                if j >= coins[i-1]:
                    dp[i][j] = dp[i-1][j]+dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        # print(dp)
        return dp[N][sum1]
