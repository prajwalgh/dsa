def feb(n):
    if n<=1:
        return n 
    return feb(n-1)+feb(n-2)
n=9
for i in range(n+1):
    print(feb(i))
