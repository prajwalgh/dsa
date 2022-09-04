# https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1
# TODO Minimize the Heights II
# Given an array arr[] denoting heights of N towers and a positive integer K.

# For each tower, you must perform exactly one of the following operations exactly once.

# Increase the height of the tower by K
# Decrease the height of the tower by K
# Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

# You can find a slight modification of the problem here.
# Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.
# User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        diff = arr[n-1]-arr[0]
        mini, maxi = arr[0], arr[n - 1]
        for i in range(1, n):
            if arr[i] < k:
                continue
            maxi = max(arr[i-1]+k, arr[-1]-k)
            mini = min(arr[0]+k, arr[i]-k)
            diff = min(diff, maxi-mini)
        return diff

# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
