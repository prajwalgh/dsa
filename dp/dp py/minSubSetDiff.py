# User function Template for python3
import math


class Solution:
    def minDifference(self, arr, n):
        sum1 = sum(arr)
        dp = [[False for i in range(sum1+1)]for i in range(n+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            for j in range(sum1+1):
                if j < arr[i-1]:
                    dp[i][j] = dp[i-1][j]
                elif j >= arr[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
        temp = []
        for i, j in enumerate(dp[-1]):
            if j == True:
                temp.append(i)
        minGlobal = float('inf')
        # /print(temp,len(temp))
        # /print(temp[:len(temp)//2],len(temp[:len(temp)//2]))
        for j in temp[:math.ceil(len(temp)/2)]:
            x = sum1-(2*j)
            # print(x)
            minGlobal = min(x, minGlobal)
        return minGlobal
