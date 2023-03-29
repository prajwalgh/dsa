# Shortest Common Supersequence

# Given two strings X and Y of lengths m and n respectively, find the length of the smallest string which has both, X and Y as its sub-sequences.
# Note: X and Y can have both uppercase and lowercase letters.
class Solution:

    # Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
        dp = [[0 for i in range(n+1)]for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if X[i-1] == Y[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        x = dp[m][n]
        return m+n-x
        # code here
