print("...............recursion.....................")


def print_val(x):
    if x < 1:
        return 0
    print(x)
    print_val(x - 1)
    # x=x+1


print_val(5)


def n_sum(x):
    if x == 0:
        return 0
    else:
        x = x + n_sum(x - 1)
    return x


print(n_sum(6))


def sumFun(i, j, sum):
    if (i == j):
        sum += i
        print(sum)
        return 0
    sum += i
    sumFun(i + 1, j, sum)
    print(i)


sumFun(1, 6, 0)


def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


print("fact is ", fact(5))

p = 0
q = 1
val = 0
n = 10
for _ in range(n):
    val = p+q
    p = q
    q = val

print("iterative Fibonacci ", val)
