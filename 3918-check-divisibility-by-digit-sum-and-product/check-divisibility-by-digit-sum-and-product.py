class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n_list = [int(x) for x in list(str(n))]
        digit_sum = 0
        digit_product = 1
        for num in n_list:
            digit_sum += num
            digit_product *= num
        return n % (digit_sum + digit_product) == 0
        