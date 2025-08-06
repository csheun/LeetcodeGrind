from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = Counter(words)
        print(word_freq)
        word_freq = sorted(Counter(words).items(), key=lambda x: (-x[1], x[0]))
        print(word_freq)
        res = [word_freq[i][0] for i in range(k)] 
        return res
            
        