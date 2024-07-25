#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#


# @lc code=start
class Solution(object):
    # def twoSum(self, nums, target):
    #     dict = {}
    #     for i in range(nums):
    #         if target - i in dict:
    #             return [i, dict[target - i]]
    #         else:
    #             dict[nums[i]] = i

    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [i, dict[target - nums[i]]]
            else:
                dict[nums[i]] = i
