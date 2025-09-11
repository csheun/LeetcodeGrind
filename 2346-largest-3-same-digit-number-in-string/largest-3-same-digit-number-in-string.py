class Solution:
    def largestGoodInteger(self, num: str) -> str:
        prev = ''
        count = 0
        res = ""
        for i in range(len(num)):
            c = num[i]
            if c != prev:
                count = 1
                prev = c
            else:
                count += 1
                if count == 3:
                    if not res:
                        res = c * 3
                    else:
                        res = max(res, c * 3)
        
        return res
