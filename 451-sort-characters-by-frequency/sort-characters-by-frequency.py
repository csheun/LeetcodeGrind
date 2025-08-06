from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        # freq = dict(Counter(s).most_common())
        freq = Counter(s)
        freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

        res_lst = []
        for key, value in freq.items():
            res_lst.append(key * value)
        return ''.join(res_lst)

