# Longest Common Subsequence

# Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.
# method 1 :recursive solution
# error :time limit exceeded
class Solution:

    # Function to find the length of longest common subsequence in two strings.
    def lcs(self, x, y, s1, s2):
        # print(x,y,s1,s2)
        if x == 0 or y == 0:
            return 0
        if s1[x-1] == s2[y-1]:
            return 1+self.lcs(x-1, y-1, s1, s2)
        else:
            return max(self.lcs(x-1, y, s1, s2), self.lcs(x, y-1, s1, s2))
        # code here


# method 2 : recursion +memoization


class Solution:
    def __init__(self):
        self.dp = [[-1 for i in range(1001)]for j in range(1001)]
    # Function to find the length of longest common subsequence in two strings.

    def lcs(self, x, y, s1, s2):
        # print(x,y,s1,s2)
        if x == 0 or y == 0:
            return 0
        if self.dp[x][y] != -1:
            return self.dp[x][y]
        if s1[x-1] == s2[y-1]:
            self.dp[x][y] = 1+self.lcs(x-1, y-1, s1, s2)
        else:
            self.dp[x][y] = max(self.lcs(x-1, y, s1, s2),
                                self.lcs(x, y-1, s1, s2))
        return self.dp[x][y]
        # code here
# methiod 3 :top down optimal


class Solution:
    # Function to find the length of longest common subsequence in two strings.
    def lcs(self, x, y, s1, s2):
        dp = [[0 for i in range(y+1)]for j in range(x+1)]
        for i in range(1, x+1):
            for j in range(1, y+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[x][y]
