#
# @lc app=leetcode id=153 lang=python
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums) not fast enough
        if (nums[0] <= nums[-1]):
            #nums is sorted
            return nums[0]
        lo = 0
        hg = len(nums)-1
        while lo <= hg:
            mid = (lo+hg)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[lo] <= nums[mid]:
                lo = mid+1
            elif nums[mid] <= nums[hg]:
                hg = mid-1
        return -1
# @lc code=end
