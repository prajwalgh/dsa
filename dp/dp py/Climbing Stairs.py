# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


from pickletools import optimize


class Solution(object):
    def climbStairs(self, n):
        def solve(n, i, dp):
            if (i == n):
                return 1
            if (i > n):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = solve(n, i+1, dp)+solve(n, i+2, dp)
            return dp[i]
        dp = [-1]*(n+1)
        ans = solve(n, 0, dp)
        return ans


# 746. Min Cost Climbing Stairs
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

class Solution(object):
    def minCostClimbingStairs(self, cost):
        # method 4 O(N) time and O(1) space
        n = len(cost)

        def solve(cost, n):
            # handel base case
            prev2 = cost[0]
            prev1 = cost[1]
            # storing values
            for i in range(2, n):
                current = cost[i]+min(prev1, prev2)
                prev2 = prev1
                prev1 = current
            return min(prev1, prev2)
        return solve(cost, n)
        # method 3 tabulation
#         n=len(cost)
#         def solve(cost,n):
#             # create dp array
#             dp=[-1]*(n+1)
#             # handel base case
#             dp[0]=cost[0]
#             dp[1]=cost[1]
#             # storing values
#             for i in range(2,n):
#                 dp[i]=cost[i]+min(dp[i-1],dp[i-2])
#             return min(dp[n-1],dp[n-2])
#         return solve(cost,n)

        # Method 2 recrtion +tabulation faster then recutuion but method 3 is even faster
        # n=len(cost)
        # dp=[-1]*(n+1)
        # def solve(cost,i,dp):
        #     if i ==0:
        #         return cost[0]
        #     if i==1:
        #         return cost[1]
        #     if dp[i]!=-1:
        #         return dp[i]
        #     dp[i]=cost[i]+min(solve(cost,i-1,dp),solve(cost,i-2,dp))
        #     return dp[i]
        # ans=min(solve(cost,n-1,dp),solve(cost,n-2,dp))
        # return ans


class Solution {

    // Space optimization solution with DP
    // T.C - O(n), S.C - O(1)
    public int climbStairs(int n) {

        if (n == 1){
            return 1
        }
        int[] dp = new int[n+1]
        int prev1 = 2
        int prev2 = 1

        for (int i=3
             i <= n
             i++){
            int curr = prev1 + prev2
            // pointer switch for next iteration
            prev2 = prev1
            prev1 = curr
        }
        return prev1
    }

    // DP solution
    public int climbStairs1(int n) {

        if (n == 1){
            return 1
        }
        int[] dp = new int[n+1]
        dp[1] = 1
        dp[2] = 2

        for (int i=3
             i <= n
             i++){
            dp[i] = dp[i-1] + dp[i-2]
        }
        return dp[n]
    }

    // Recursion+Memoization solution
    public int climbStairs2(int n) {
        int[] dp = new int[n+1]
        for (int i=0
             i <= n
             i++){
            dp[i] = -1
        }
        return solve(n, dp)
    }

    int solve(int n, int[] dp){

        // base cases
        if (n < 0){
            return 0
        }
        if (n == 0){
            return 1
        }

        if (dp[n] != -1)
        return dp[n]

        dp[n] = solve(n-1, dp) + solve(n-2, dp)
        return dp[n]
    }


}


# 70. Climbing Stairs
# efficient java soltion using DP - with Time and Space optimization
# fastest optimizeed solutoon for climbing stairs
class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        prev1 = 2
        prev2 = 1
        for i in range(3, n+1):
            current = prev1+prev2
            prev2 = prev1
            prev1 = current
        return prev1
# class Solution {

#     // Space optimization solution with DP
#     // T.C - O(n), S.C - O(1)
#     public int climbStairs(int n) {

#         if (n == 1){
#             return 1
#         }
#         int[] dp = new int[n+1]
#         int prev1 = 2
#         int prev2 = 1

#         for (int i=3
#              i <= n
#              i++){
#             int curr = prev1 + prev2
#             // pointer switch for next iteration
#             prev2 = prev1
#             prev1 = curr
#         }
#         return prev1
#     }

#     // DP solution
#     public int climbStairs1(int n) {

#         if (n == 1){
#             return 1
#         }
#         int[] dp = new int[n+1]
#         dp[1] = 1
#         dp[2] = 2

#         for (int i=3
#              i <= n
#              i++){
#             dp[i] = dp[i-1] + dp[i-2]
#         }
#         return dp[n]
#     }

#    	// Recursion+Memoization solution
#     public int climbStairs2(int n) {
#         int[] dp = new int[n+1]
#         for (int i=0
#              i <= n
#              i++){
#             dp[i] = -1
#         }
#         return solve(n, dp)
#     }

#     int solve(int n, int[] dp){

#         // base cases
#         if (n < 0){
#             return 0
#         }
#         if (n == 0){
#             return 1
#         }

#         if (dp[n] != -1)
#         return dp[n]

#         dp[n] = solve(n-1, dp) + solve(n-2, dp)
#         return dp[n]
#     }


# }
