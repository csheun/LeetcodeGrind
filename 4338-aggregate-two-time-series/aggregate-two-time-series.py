class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        ptr_1, ptr_2 = 0, 0
        n_1 = len(series1)
        n_2 = len(series2)
        res = []
        while ptr_1 < n_1 and ptr_2 < n_2:
            curr = []
            if series1[ptr_1][0] < series2[ptr_2][0]:
                curr = [series1[ptr_1][0], series1[ptr_1][1] + series2[ptr_2][1]]
                ptr_1 += 1
            elif series1[ptr_1][0] == series2[ptr_2][0]:
                curr = [series1[ptr_1][0], series1[ptr_1][1] + series2[ptr_2][1]]
                ptr_1 += 1
                ptr_2 += 1
            else:
                curr = [series2[ptr_2][0], series1[ptr_1][1] + series2[ptr_2][1]]
                ptr_2 += 1
            res.append(curr)
        # clean up remaining
        while ptr_1 < n_1:
            res.append(series1[ptr_1])
            ptr_1 += 1
        while ptr_2 < n_2:
            res.append(series2[ptr_2])
            ptr_2 += 1
        
        return res

        