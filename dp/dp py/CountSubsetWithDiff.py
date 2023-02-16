
arr = [1, 2, 3, 1, 2]  # # [1, 1, 2, 3]  #
diff = 1    # 1
sum1 = (diff + sum(arr))//2
dp = [[0 for i in range(sum1+1)] for j in range(len(arr)+1)]
dp[0][0] = 1
for i in range(1, len(arr)+1):
    for j in range(sum1+1):
        if j < arr[i-1]:
            dp[i][j] = dp[i-1][j]
        elif j >= arr[i-1]:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
print(dp)
print(dp[sum1][len(arr)])
