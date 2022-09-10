# 198. House Robber

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        prev1 = 0
        prev2 = nums[0]
        for i in range(1, len(nums)):
            curr = max(prev2, prev1+nums[i])
            prev1 = prev2
            prev2 = curr
        return prev2


# 213. House Robber II
# Medium

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]

        def helper(nums):
            if len(nums) == 0:
                return 0
            prev1 = 0
            prev2 = nums[0]
            for i in range(1, len(nums)):
                curr = max(prev2, prev1+nums[i])
                prev1 = prev2
                prev2 = curr
            return prev2
        return max(helper(nums[1:]), helper(nums[:-1]))
        # temp=helper(nums[0:n-1])
        # print(temp)
        # if temp<helper(nums[1:n]):
        #     temp=helper(nums[1:n])
        #     return temp
        # return temp
