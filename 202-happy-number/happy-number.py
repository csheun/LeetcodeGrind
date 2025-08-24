class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)

        while n != 1:
            next_sum = 0
            while n > 0:
                digit = n % 10
                next_sum += digit ** 2
                n //= 10
            if next_sum in seen:
                return False
            n = next_sum
            seen.add(n)
        
        return True




        

        return True
        