# 1383. Maximum Performance of a Team
# You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

# Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

# The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

# Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.


# Example 1:

# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
# Output: 60
# Explanation:
# We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
import heapq


class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        eng = []
        for i, j in zip(efficiency, speed):
            eng.append([i, j])
        eng.sort(reverse=True)
        res, speed = 0, 0
        minheap = []
        for eff, spd in eng:
            if len(minheap) == k:
                speed -= heapq.heappop(minheap)
            speed += spd
            heapq.heappush(minheap, spd)
            res = max(res, eff*speed)
        return res % (10**9+7)
