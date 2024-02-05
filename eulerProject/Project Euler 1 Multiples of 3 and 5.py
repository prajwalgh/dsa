t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    def sum_of_mul(k):
        p = (n - 1) // k
        return k * (p * (p + 1)) // 2

    res = sum_of_mul(3) + sum_of_mul(5) - sum_of_mul(15)
    print(res)
    # total_sum=0
    # for i in range(n):
    #     if i%3==0 or i%5==0:
    #         total_sum+=i
    # print(total_sum)
