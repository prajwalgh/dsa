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


# 740. Delete and Earn
# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.


class Solution(object):
    def deleteAndEarn(self, nums):
        counts, k = Counter(nums), max(nums)
        print(counts)
        dp0, dp1 = 0, counts[1]
        for i in range(2, k+1):
            dp0, dp1 = dp1, max(dp1, dp0+i*counts[i])
        return dp1


# 55. Jump Game
# Medium
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.


# Example 1:

# Input: nums = [2, 3, 1, 1, 4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


class Solution(object):
    def canJump(self, nums):
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i] >= goal:
                goal = i
        if goal == 0:
            return True
        else:
            return False


# dp solution
# below code in c++
# class Solution(object):
#       def canJump( nums) :
#         dp=[o]*(len(nums)+1)
#         dp[0].first = 1
#         dp[0].second = nums[0]
#         for (int i=1
#              i < nums.size()
#              i++) {
#             if (dp[i - 1].second >= i) {
#                 dp[i].first = 1
#                 dp[i].second = max(dp[i-1].second, i + nums[i])
#             }
#             else {
#                 dp[i].first = 0
#                 dp[i].second = 0
#             }
#         }
#         return dp[nums.size() - 1].first
#     }
# }
