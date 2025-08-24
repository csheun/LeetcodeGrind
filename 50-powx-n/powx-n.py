class Solution:
    def myPow(self, x: float, n: int) -> float:
        print(n)
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        if n % 2 == 1:
            return x * self.myPow(x, n - 1)
        half = self.myPow(x, n // 2)
        return half * half
        