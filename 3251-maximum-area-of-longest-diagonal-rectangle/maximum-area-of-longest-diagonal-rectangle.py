class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = 0
        max_diag = 0
        for dim in dimensions:
            dia_squared = dim[0] ** 2 + dim[1] ** 2
            area = dim[0] * dim[1]
            if dia_squared > max_diag:
                max_diag = dia_squared
                max_area = area
            elif dia_squared == max_diag:
                max_area = max(max_area, area)
        return max_area