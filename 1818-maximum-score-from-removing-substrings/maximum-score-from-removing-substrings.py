class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def helper(s: str, pattern: str, score: int):
            stack = []
            gain = 0
            for i in range(len(s)):
                top = stack[-1] if stack else ''
                if pattern == top + s[i]:
                    gain += score
                    stack.pop()
                else:
                    stack.append(s[i])
            return ''.join(stack), gain
        
        if (x >= y):
            # clear 'ab' before 'ba'
            s, gain_1 = helper(s, 'ab', x)
            _, gain_2 = helper(s, 'ba', y)
        else:
            s, gain_1 = helper(s, 'ba', y)
            _, gain_2 = helper(s, 'ab', x)
        
        return gain_1 + gain_2
