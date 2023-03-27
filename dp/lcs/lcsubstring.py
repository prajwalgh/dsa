# Longest Common Substring
# MediumAccuracy: 42.69 % Submissions: 150K+Points: 4
# Win Prize worth ₹6000 with Ease. Register for the Easiest Coding Challenge!

# Given two strings. The task is to find the length of the longest common substring.


class Solution:
    def longestCommonSubstr(self, s1, s2, n, m):
        dp = [[0 for i in range(m+1)]for j in range(n+1)]
        max1 = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                    if dp[i][j] > max1:
                        max1 = dp[i][j]
        # print(dp)
        # x=max(map(max, dp))
        return max1
