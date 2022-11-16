#
# @lc app=leetcode id=374 lang=python
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        if guess(n) == 0:
            return n
        i=1
        m=i
        while i<n:
            print(m)
            if guess(m) == 0:
                return m
            if guess(m) ==1:
                i=m
            if guess(m) == -1:
                n=m
            m=(i+n)//2
                
        
# @lc code=end

