#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        def unique(s):
            x = list(s)
            y = set(s)
            return len(x) == len(y)

        i = 0
        ans = 0
        for j in range(1, len(s) + 1):
            print(s[i:j])
            if unique(s[i:j]):
                ans = max(ans, len(s[i:j]))
            else:
                i += 1
        return ans

    # @lc code=end
