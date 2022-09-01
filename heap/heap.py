a = [2,0, 66, 30, 5, 9, 10,99,8,55,223]
n = len(a)

def max_heapify(a,n,i):
        largest=i
        left=i*2+1
        right=i*2+2
        if left<n and a[left]>a[largest]:
            largest=left
        if right<n and a[right]>a[largest]:
            largest=right
        if largest!=i:
            a[i],a[largest]=a[largest],a[i]
            max_heapify(a,n,largest)

#for i in range(n // 2 - 1, -1, -1):
#    max_heapify(a,n,i)

print("MAX hip")
for i in range(n):
    print(a[i])


def min_heapify(a, n, i):
    smallest = i
    left = i * 2 + 1
    right = i * 2 + 2
    if left < n and a[left]<smallest:
        smallest=left
    if right < n and a[right] < smallest:
            smallest = right
    if smallest != i:
        a[i], a[smallest] = a[smallest], a[i]
        max_heapify(a, n, smallest)

for i in range(n//2-1,-1,-1):
    min_heapify(a,n,i)

print("MIN hip")
for i in range(n):
    print(a[i])
