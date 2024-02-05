t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    p1 = 1
    p2 = 2
    feb = p1 + p2
    ans = 2
    while feb <= n:
        if feb % 2 == 0:
            ans += feb
        p1 = p2
        p2 = feb
        feb = p1 + p2
    print(ans)
