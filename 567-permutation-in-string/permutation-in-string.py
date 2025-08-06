from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False
        s1_freq = Counter(s1)
        word_len = len(s1)
        curr_freq = {}
        for i in range(len(s2)):
            if s2[i] not in curr_freq:
                curr_freq[s2[i]] = 0
            curr_freq[s2[i]] += 1
            if i >= len(s1) - 1:
                #long enough
                if (curr_freq == s1_freq):
                    return True
                else:
                    curr_freq[s2[i - len(s1) + 1]] -= 1
                    if curr_freq[s2[i - len(s1) + 1]] == 0:
                        del curr_freq[s2[i - len(s1) + 1]]
        return False
                

        