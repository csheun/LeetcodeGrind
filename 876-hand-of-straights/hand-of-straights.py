from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # # 1) Repeatedly find the smallest element and try to form a sequence (total time affected by the (n / groupsize) * O(n) for finding the min element)
        # n = len(hand)
        # if (n % groupSize != 0):
        #     return False
        # freq = Counter(hand)
        # # find smallest element and remove the rest
        # while freq:
        #     smallest = min(freq.keys())
        #     for i in range(groupSize):
        #         target = smallest + i
        #         if target in freq:
        #             freq[target] -= 1
        #             if freq[target] == 0:
        #                 del freq[target]
        #         else:
        #             return False
        # return True

        # 2) sort the array and form the sequence
        if (len(hand) % groupSize != 0):
            return False

        freq = Counter(hand)
        hand.sort()

        for i in range(len(hand)):
            # will always be the smallest element so far
            if freq[hand[i]] > 0:
                count = freq[hand[i]]
                for j in range(groupSize):
                    num = hand[i] + j
                    if freq[num] < count:
                        return False
                    else:
                        freq[num] -= count
        return True
        