class Solution:
    def matrixMultiplication(self, N, arr):
        def solve(arr, i, j, dp):
            if i == j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            min1 = float("inf")
            for k in range(i, j):
                temp = (
                    solve(arr, i, k, dp)
                    + solve(arr, k + 1, j, dp)
                    + (arr[i - 1] * arr[j] * arr[k])
                )
                if min1 > temp:
                    min1 = temp
                dp[i][j] = min1
            return min1

        dp = [[-1] * N for _ in range(N)]
        return solve(arr, 1, len(arr) - 1, dp)


a = Solution()
N = 4
arr = [10, 30, 5, 60]
print(a.matrixMultiplication(N, arr))
