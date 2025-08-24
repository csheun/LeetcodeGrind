class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        add_one = digits[-1] + 1
        carry = add_one // 10
        digits[-1] = add_one % 10

        for i in range(len(digits) - 2, -1, -1):
            if not carry:
                break
            add_one = digits[i] + carry
            carry = add_one // 10
            digits[i] = add_one % 10
        
        if carry:
            digits.insert(0, 1)
        
        return digits