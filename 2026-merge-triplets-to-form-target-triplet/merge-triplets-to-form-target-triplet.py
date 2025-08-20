class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # loop through and find if there are triplets that satisfy the condtion whrby any idx == target idx and the other 2 indexes are = or < than
        # need all three idxes fulfilled

        def checkTriplets(triplet: List[int]):
            res = []
            for i in range(len(triplet)):
                if triplet[i] == target[i]:
                    res.append(i)
                if (triplet[i] > target[i]):
                    return []
            return res
        
        goal = set([_ for _ in range(len(triplets[0]))])
        res = set()
        for triplet in triplets:
            valid_idxes= checkTriplets(triplet)
            for idx in valid_idxes:
                res.add(idx)
            if (res == goal):
                return True
        return False
            

        