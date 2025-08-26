class Solution:
    def mySqrt(self, x: int) -> int:
        # use binary search
        lo = 0
        hi = x

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            print(f'lo: {lo}, hi: {hi}, mid: {mid}')
            squared = mid * mid
            if squared == x:
                return mid
            elif squared < x:
                lo = mid + 1
            else:
                hi = mid -1

        return lo - 1
            