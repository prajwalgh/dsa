#
# @lc app=leetcode id=451 lang=python
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(c*fre for c, fre in Counter(s).most_common())
        # count=Counter(s)
        # y=OrderedDict(count.most_common())
        # a=y.keys()
        # ans=''
        # for i in a:
        #     i=i*count[i]
        #     ans=ans+i
        # return ans

# @lc code=end
