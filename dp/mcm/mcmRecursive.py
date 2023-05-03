class Solution:
    def matrixMultiplication(self, N, arr):
        def solve(arr, i, j):
            if i == j:
                return 0
            min1 = [float("inf")]
            for k in range(i, j):
                temp = (
                    solve(arr, i, k)
                    + solve(arr, k + 1, j)
                    + (arr[i - 1] * arr[j] * arr[k])
                )
                # print(temp)
                if min1[0] > temp:
                    min1[0] = temp
            return min1[0]

        return solve(arr, 1, len(arr) - 1)


a = Solution()
N = 4
arr = [10, 30, 5, 60]
print(a.matrixMultiplication(N, arr))
