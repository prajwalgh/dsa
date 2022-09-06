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

# 1480. Running Sum of 1d Array


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i]+nums[i-1]
        return nums


# 205. Isomorphic Strings

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
` `


class Solution(object):
    def isIsomorphic(self, s, t):
        dict_s = dict()
        count_s = 0
        dict_t = dict()
        count_t = 0

        for i in s:
            if i not in dict_s:
                dict_s[i] = count_s
                count_s += 1
            else:
                continue

        for i in t:
            if i not in dict_t:
                dict_t[i] = count_t
                count_t += 1
            else:
                continue
        list_s = list()
        for i in s:
            list_s.append(dict_s[i])

        list_t = list()
        for i in t:
            list_t.append(dict_t[i])

        if list_s == list_t:
            return True
        else:
            return False


# 392. Is Subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


class Solution(object):
    def isSubsequence(self, s, t):
        sq = s
        tq = t
        i = 0
        j = 0
        while i < len(sq) and j < len(tq):
            if sq[i] == tq[j]:
                i += 1
            j += 1

        if i == len(sq):
            return True
        else:
            return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
