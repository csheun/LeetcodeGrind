from collections import defaultdict
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        beautiful_substrings = []
        freq = defaultdict(int)
        l = 0 
        for i in range(len(s)):
            c = s[i]
            if c == '0':
                if freq['1'] == 0:
                    l += 1
                    continue
                freq[c] += 1
            if c == '1':
                freq[c] += 1
                if freq[c] < k:
                    continue
                elif freq[c] == k:
                    #found, record down
                    beautiful_substrings.append(s[l:i + 1])
                else:
                    # > k, exceed, need to move pointer to the next 1s (now is cfm pointing at a 1)
                    while True:
                        freq[s[l]] -= 1
                        l += 1
                        if s[l] == '1':
                            break
                    if freq['1'] == k:
                        beautiful_substrings.append(s[l:i + 1])

        print(beautiful_substrings)

        if beautiful_substrings:
            beautiful_substrings.sort(key=lambda x: int(x, 2))
            return beautiful_substrings[0]
        return ''
                

        