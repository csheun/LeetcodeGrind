class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # intuition: 1) k is <=  maximum value of piles
        # exp: if is > max value of piles then it can defo finish eating within
        # len(piles) hours which is <= h
        # but we want minimum integer K

        def calcEatingTime(piles: List[int], speed: int) -> int:
            hours = 0
            for pile in piles:
                if (pile <= speed):
                    hours += 1
                else:
                    hours += ceil(pile / speed)
            return hours
                
        lo = 1
        hi = max(piles)

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            curr_time = calcEatingTime(piles, mid)

            if (curr_time > h):
                # increase eating speed
                lo = mid + 1
            elif (curr_time <= h):
                # check if there is a slower speed that within h
                if (mid == 1):
                    return mid
                prev_speed_time = calcEatingTime(piles, mid - 1)
                if (prev_speed_time > h):
                    return mid
                else:
                    hi = mid - 1
        return -1
        