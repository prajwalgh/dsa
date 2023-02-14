# Given an array arr[] of length N and an integer X, the task is to find the number of subsets with a sum equal to X.
def perfectSum(arr, N, x):
    # code here
    dp = ([[0 for i in range(x+1)] for i in range(N+1)])
    dp[0][0] = 1
    for i in range(1, x+1):
        dp[0][i] = 0
    for i in range(1, N+1):
        for j in range(x+1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            elif j >= arr[i-1]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
    return dp[N][x]


a = [1, 2, 3, 4]
n = 4
sum = 5
print(perfectSum(a, n, sum))


class Solution:
    def perfectSum(self, arr, N, x):
        # code here
        dp = ([[0 for i in range(x+1)] for i in range(N+1)])
        dp[0][0] = 1
        for i in range(1, N+1):
            for j in range(x+1):
                if j < arr[i-1]:
                    dp[i][j] = dp[i-1][j]
                elif j >= arr[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
        return dp[N][x] % (10**9+7)
