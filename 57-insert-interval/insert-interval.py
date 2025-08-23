class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # add the newInterval into the intervals first 
        lo = 0
        hi = len(intervals) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if intervals[mid][0] < newInterval[0]:
                lo = mid + 1
            else:
                hi = mid - 1

        intervals.insert(lo, newInterval)

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            prev = res[-1]
            curr = intervals[i]
            # if overlap calculate new range and replace prev
            # else just add
            # overlap -> later start is <= ealier end

            if max(prev[0], curr[0]) <= min(prev[1], curr[1]):
                new_range = [min(prev[0], curr[0]), max(prev[1], curr[1])]
                res[-1] = new_range
            else:
                res.append(curr)    
        

        return res