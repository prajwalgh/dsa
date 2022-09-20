class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        strnum2 = ''.join([chr(x) for x in nums2])
        print(strnum2)
        strmax = ''
        ans = 0
        for num in nums1:
            strmax += chr(num)
            if strmax in strnum2:
                ans = max(ans, len(strmax))
            else:
                strmax = strmax[1:]
        return ans
# on liner
        # class Solution:
#     def findLength(self, n1: List[int], n2: List[int]) -> int:
#         return max(reduce(lambda l, e: [0, *((e==f)*(l+1) for l, f in zip(l, n1)), max(l)], n2, [0 for _ in n1])) \

# dp solutioon

# class Solution(object):
#     def findLength(self, A, B):
#         dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
#         for i in range(1, len(A) + 1):
#             for j in range(1, len(B) + 1):
#                 if A[i - 1] == B[j - 1]:
#                     dp[i][j] = dp[i - 1][j - 1] + 1
#         return max(max(row) for row in dp)
