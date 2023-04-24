#
# @lc app=leetcode id=1046 lang=python
#
# [1046] Last Stone Weight
#


# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            temp1 = stones.pop()
            temp2 = stones.pop()
            if temp1 != temp2:
                stones.append(abs(temp2 - temp1))
        return stones[0] if stones else 0


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert the list of stones into a max heap
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        # Repeatedly pop the two heaviest stones and add the difference back to the heap
        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            if stone1 != stone2:
                heapq.heappush(heap, -(stone1 - stone2))

        # Return the final weight of the remaining stone, if any
        return -heap[0] if heap else 0


# @lc code=end
