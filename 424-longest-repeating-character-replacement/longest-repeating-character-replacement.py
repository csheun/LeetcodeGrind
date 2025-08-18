class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # hashtable tl track frequency of letters in curr subarray
        # sliding window to track subarray
        # 1) if curr subarray len - max_freq <= k then is fine
        # 2) else need to shorten subarray 

        letter_freq = {}
        res = 0
        i = 0
        for j in range(len(s)):
            letter_freq[s[j]] = letter_freq.get(s[j], 0) + 1
            max_freq = max(letter_freq.values())
            curr_len = j - i + 1
            if (curr_len - max_freq > k):
                # exceed need to shorten sliding window
                letter_freq[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res




        