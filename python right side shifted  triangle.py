n=5
# python right side shifted  triangle
#   *
#  **
# ***
#****

for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(i,n):
        print("*",end=" ")
    print()
