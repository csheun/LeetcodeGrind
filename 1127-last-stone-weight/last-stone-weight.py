import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heapq.heappush(pq, -stone)
        
        while (len(pq) >= 2):
            stone_1 = abs(heapq.heappop(pq))
            stone_2 = abs(heapq.heappop(pq))
            remaining = stone_1 - stone_2
            print(f"stone1: {stone_1}, stone2: {stone_2}, remaining: {remaining}")
            if remaining > 0:
                heapq.heappush(pq, -remaining)
        if not pq:
            return 0
        return abs(pq[0])

        