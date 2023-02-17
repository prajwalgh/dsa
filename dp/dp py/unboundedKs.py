# 14 Rod Cutting Problem is nothing but unbounded knapsack problem


n = 2
W = 100
val = [1, 30]
wt = [1, 50]
K = [[0 for x in range(W + 1)] for x in range(n + 1)]
#K[0][0] = 1

# Build table K[][] in bottom up manner
for i in range(n + 1):
    for w in range(W + 1):
        if i == 0 or w == 0:
            K[i][w] = 0
        elif wt[i - 1] <= w:
            K[i][w] = max(val[i - 1]
                          + K[i][w - wt[i - 1]],
                          K[i - 1][w])
        else:
            K[i][w] = K[i - 1][w]

print(K)
print(K[n][W])
