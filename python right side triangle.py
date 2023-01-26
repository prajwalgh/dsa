n=5
# python right side triangle
#   *
#  **
# ***
#****

for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
