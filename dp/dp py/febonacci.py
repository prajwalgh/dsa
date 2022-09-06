def feb(n):
    if n <= 1:
        return n
    return feb(n-1)+feb(n-2)


n = 9
for i in range(n+1):
    print(feb(i))
# 1137. N-th Tribonacci Number

# The Tribonacci sequence Tn is defined as follows:

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.


class Solution(object):
    def tribonacci(self, n):
        if n <= 1:
            return n
        if n == 2:
            return 1
        prev3 = 0
        prev2 = 1
        prev1 = 1
        for i in range(2, n):
            curr = prev1+prev2+prev3
            prev3 = prev2
            prev2 = prev1
            prev1 = curr
        return prev1
