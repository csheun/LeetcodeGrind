class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            last = res[len(res) - 1]
            new = [1]
            for i in range(0, len(last) - 1):
                val = last[i] + last[i + 1]
                new.append(val)
            new.append(1)
            res.append(new)
        return res

        