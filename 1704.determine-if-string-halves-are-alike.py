#
# @lc app=leetcode id=1704 lang=python
#
# [1704] Determine if String Halves Are Alike
#

# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        len1 = len(s)
        a = s[0:len1//2]
        b = s[len1//2:]
        vov = ["a", "e", "i", "o", "u"]
        cout_a = 0
        cout_b = 0
        for i in a:
            if i in vov:
                cout_a += 1
        for i in b:
            if i in vov:
                cout_b += 1
        if cout_a == cout_b:
            return True
        else:
            return False
# @lc code=end
