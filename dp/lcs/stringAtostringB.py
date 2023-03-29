# Minimum number of deletions and insertions.
# EasyAccuracy: 65.29 % Submissions: 34K+Points: 2
# Attend free LIVE Webinars with Summer Skill-Up Sessions! Enroll Now!

# Given two strings str1 and str2. The task is to remove or insert the minimum number of characters from / in str1 so as to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted to some another point.
# User function Template for python3
class Solution:
    def minOperations(self, s1, s2):
        r = len(s1)
        c = len(s2)
        dp = [[0 for i in range(c+1)]for j in range(r+1)]
        for i in range(1, r+1):
            for j in range(1, c+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
       # print(dp)
        return r+c-dp[-1][-1]-dp[-1][-1]
