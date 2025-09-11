class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # group all the same ans together
        ans_freq = Counter(answers)
        res = 0
        for ans, freq in ans_freq.items():
            if freq <= ans + 1:
                res += ans + 1
            else:
                # ans = 1 but there are 5 ppl saying 1
                res += ceil(freq / (ans + 1)) * (ans + 1)
        return res
        