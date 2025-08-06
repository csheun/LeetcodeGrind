class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        count = 0
        char_dict= {}
        i = 0
        for j in range(len(s)):
            if s[j] in char_dict:
                max_count = max(max_count, count)
                # move left pointer to the repeated index
                target_idx = char_dict[s[j]]
                while (i <= target_idx):
                    del char_dict[s[i]]
                    count -= 1
                    i += 1
            count += 1
            char_dict[s[j]] = j
        max_count = max(max_count, count)
        return max_count
            
        