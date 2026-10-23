class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # stack contains '(', ')', numbers
        # when ')' evaluate straightaway -> if () then = 1
        # if numbers then add up until an opening bracket reach
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
                continue
            # c == ')'
            # check top of stack
            if stack[-1] == '(':
                stack.pop()
                stack.append(1)
            else:
                # add up the numbers until a opening bracket then * 2
                digits_sum = 0
                while stack[-1] != '(':
                    digits_sum += stack.pop()
                # remove the '('
                stack.pop()
                stack.append(digits_sum * 2)
        return sum(stack)
            
        