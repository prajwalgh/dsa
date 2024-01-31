class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        # Method 2: O(N)
        n = len(temp)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and temp[i] > temp[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans


# Method 1 : brute force O(N^2)
# ans=[]
# for i in range(len(temp)):
#     j=i+1
#     prevLen=len(ans)
#     while j<len(temp):
#         if temp[i]<temp[j]:
#             ans.append(j-i)
#             break
#         j+=1
#     if prevLen==len(ans):
#         ans.append(0)
# return ans
