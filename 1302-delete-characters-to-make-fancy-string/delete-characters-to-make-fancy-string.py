class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ''
        curr_char = ''
        curr_count = 0
        for i in range(len(s)):
            if s[i] == curr_char:
                if curr_count >= 2:
                    continue
                else:
                    res += s[i]
                    curr_count += 1
            else:
                res += s[i]
                curr_char = s[i]
                curr_count = 1
                
        return res
                

