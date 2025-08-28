class Solution:
    def canAliceWin(self, n: int) -> bool:
        stone = 10
        while n >= stone:
            n -= stone
            stone -= 1

        
        return stone % 2 == 1
        