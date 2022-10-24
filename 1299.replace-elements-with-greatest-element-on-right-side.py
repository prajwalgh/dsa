#
# @lc app=leetcode id=1299 lang=python
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # mehod one brute force O(n^2)
        # for i in range(len(arr)-1):
        #     arr[i]=max(arr[i+1:])
        # arr[-1]=-1
        # return arr
        # method 2 revese
        max1 = -1
        for i in range(len(arr)-1, -1, -1):
            max1 = max(max1, arr[i])
            arr[i] = max1
        arr.append(-1)
        return arr[1:]

# @lc code=end
