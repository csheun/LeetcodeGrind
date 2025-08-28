class Solution:
    def digitCount(self, num: str) -> bool:
        freq = Counter(num)
        for i in range(len(num)):
            freq_of_idx = int(num[i])
            freq_in_num = freq.get(str(i), 0)
            if freq_of_idx != freq_in_num:
                return False
        return True
                
        