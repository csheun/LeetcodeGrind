from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if (n % groupSize != 0):
            return False
        freq = Counter(hand)
        # find smallest element and remove the rest
        while freq:
            smallest = min(freq.keys())
            for i in range(groupSize):
                target = smallest + i
                if target in freq:
                    freq[target] -= 1
                    if freq[target] == 0:
                        del freq[target]
                else:
                    return False
        return True

        