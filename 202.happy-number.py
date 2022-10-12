#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def squadd(self, a):
        s = 0
        for i in a:
            i = int(i)
            i = i*i
            s = s+i
        return s

    def isHappy(self, n: int) -> bool:
        a = str(n)
        cycle = []
        s = self.squadd(a)
        if s == 1:
            return True
        while s != 1:
            s = self.squadd(str(s))
            if s in cycle:
                return False
            cycle.append(s)
            if s == 1:
                return True
# @lc code=end
