class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = 0

        for fruit in fruits:
            # loop through basket to find a place:
            placed = False
            for i in range(len(baskets)):
                if fruit <= baskets[i]:
                    baskets[i] = -1
                    placed = True
                    break
            if not placed:
                res += 1
        
        return res