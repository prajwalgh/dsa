#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,r=0,len(matrix[0])-1
        t,b=0,len(matrix)-1      
        output=[]
        step=0
        while l<=r and t<=b:
            match(step%4):
                case 0:
                    for i in range(l,r+1):
                        output.append(matrix[t][i])
                    t+=1
                case 1:
                    for i in range(t,b+1):
                        output.append(matrix[i][r])
                    r-=1
                case 2:
                    for i in range(r,l-1,-1):
                        output.append(matrix[b][i])
                    b-=1
                case 3:
                    for i in range(b, t-1, -1):
                        output.append(matrix[i][l])
                    l += 1
            step += 1
        return output      
# @lc code=end

