from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = Counter(s)
        res = []
        count = 0
        pending_chars = set()
        chars_freq = {}
        for i in range(len(s)):
            c = s[i]
            count += 1
            pending_chars.add(c)
            if c not in chars_freq:
                chars_freq[c] = 0
            chars_freq[c] += 1
            if (chars_freq[c] == freq[c]):
                pending_chars.remove(c)
            if not pending_chars:
                res.append(count)
                count = 0
        return res

            
        