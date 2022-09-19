#
# @lc app=leetcode id=918 lang=python
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        totalSum = 0
        minEndingHere = maxEndingHere = 0
        minimum, maximum = float("inf"), float("-inf")
        for num in nums:
            totalSum += num
            minEndingHere = min(minEndingHere+num, num)
            maxEndingHere = max(maxEndingHere+num, num)
            minimum = min(minimum, minEndingHere)
            maximum = max(maximum, maxEndingHere)

        return max(maximum, totalSum-minimum) if maximum >= 0 else maximum


# @lc code=end
s1 = Solution()
nums = [1, -2, 3, -2]
print(s1.maxSubarraySumCircular(nums))
