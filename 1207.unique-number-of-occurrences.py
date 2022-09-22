#
# @lc app=leetcode id=1207 lang=python
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution(object):
    def uniqueOccurrences(self, arr):
        # this method is python specific as is fast
        counter = Counter(arr)
        if len(counter.values()) == len(set(counter.values())):
            return True
        else:
            return False
# @lc code=end
