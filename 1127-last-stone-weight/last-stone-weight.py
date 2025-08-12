import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-x for x in stones]
        # heapify() runs in O(n) time use this
        heapify(pq)
        while (len(pq) >= 2):
            stone_1 = abs(heapq.heappop(pq))
            stone_2 = abs(heapq.heappop(pq))
            remaining = stone_1 - stone_2
            if remaining > 0:
                heapq.heappush(pq, -remaining)
        if not pq:
            return 0
        return abs(pq[0])

        