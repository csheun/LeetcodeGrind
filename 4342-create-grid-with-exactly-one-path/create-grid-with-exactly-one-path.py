class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # simple route -> move left and move down
        res = []
        res.append("." * n)
        path = "#" * (n - 1) + "."
        for _ in range(1, m):
            res.append(path)
        return res
        