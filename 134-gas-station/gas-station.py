class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # intuition: get the difference bettwen gas and cost
        # find an index to add the diff clockwise such that the sum will nvr be -ve at any point

        # key point is: at any index current gas becomes -ve, means all idx between ith and starting point are bad, including starting point 
        # starting point at A: A + B + C is +ve then A + B + C + D is -ve,
        # B + C will always be < A + B + C as A is +ve (if not the condition will fail early) so if A + B + C + D is -ve then B + C + D is -ve so 
        # point A, B, C, D all cannot be starting point

        diff = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(diff) < 0:
            return -1
        curr_gas = 0
        i = 0
        n = len(diff)
        while i < n:
            curr_gas = 0
            for j in range(n):
                curr_gas += diff[(i + j) % n]
                if curr_gas < 0:
                    i = (i + j) % n + 1
                    break
            if curr_gas >= 0:
                return i 
        return -1
