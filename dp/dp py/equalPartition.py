class Solution:
    def equalPartition(self, N, arr):
        x = sum(arr)
        # print(x)
        if x % 2 != 0:
            return False
        else:
            x = x//2
            # print(x)
            dp = ([[True for i in range(x+1)] for i in range(N+1)])
            for i in range(N+1):
                dp[i][0] = True
            for i in range(1, x+1):
                dp[0][i] = False
            for i in range(1, N+1):
                for j in range(1, x+1):
                    if j < arr[i-1]:
                        dp[i][j] = dp[i-1][j]
                    elif j >= arr[i-1]:
                        dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            return dp[N][x]


# Dynamic Programming based python
# program to partition problem

# Returns true if arr[] can be
# partitioned in two subsets of
# equal sum, otherwise false


def findPartition(arr, n):
    sum = 0
    i, j = 0, 0

    # calculate sum of all elements
    for i in range(n):
        sum += arr[i]

    if sum % 2 != 0:
        return false

    part = [[True for i in range(n + 1)]
            for j in range(sum // 2 + 1)]

    # initialize top row as true
    for i in range(0, n + 1):
        part[0][i] = True

    # initialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, sum // 2 + 1):
        part[i][0] = False

    # fill the partition table in
    # bottom up manner
    for i in range(1, sum // 2 + 1):

        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]

            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or
                              part[i - arr[j - 1]][j - 1])

    return part[sum // 2][n]


# Driver Code
arr = [3, 1, 1, 2, 2, 1]
n = len(arr)

# Function call
if findPartition(arr, n) == True:
    print("Can be divided into two",
          "subsets of equal sum")
else:
    print("Can not be divided into ",
          "two subsets of equal sum")

# This code is contributed
# by mohit kumar 29
