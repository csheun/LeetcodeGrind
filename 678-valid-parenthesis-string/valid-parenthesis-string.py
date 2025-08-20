class Solution:
    def checkValidString(self, s: str) -> bool:
        # c_min is the minimum ')' we must encounter
        # c_max is the maximum ')' we can encounter
        c_min = c_max = 0
        for c in s:
            match c:
                case '(':
                    c_min += 1
                    c_max += 1
                case ')':
                    c_min -= 1
                    c_max -= 1
                case '*':
                    # when * is ')'
                    c_min -= 1
                    # min cannot be < 0
                    # when * is '('
                    c_max += 1
            c_min = max(c_min, 0)
            if c_max < 0:
                return False
        return c_min == 0


        