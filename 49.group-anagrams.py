#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            dic[tuple(count)].append(s)
        return dic.values()

        # dict_s = {}
        # for s in strs:
        #     sort_s = "".join(sorted(s))
        #     if sort_s in dict_s:
        #         dict_s[sort_s].append(s)
        #     else:
        #         dict_s[sort_s] = [s]
        # return list(dict_s.values())
# @lc code=end
