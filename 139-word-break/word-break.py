from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set()
        max_word_len = len(wordDict[0])
        min_word_len = len(wordDict[0])
        for word in wordDict:
            word_set.add(word)
            max_word_len = max(max_word_len, len(word))
            min_word_len = min(min_word_len, len(word))
        queue = deque()
        queue.append(s)
        visited = set()
        visited.add(s)
        while queue:
            curr_word = queue.popleft()
            for i in range(min_word_len, max_word_len +1):
                target = curr_word[:i]
                if target in word_set:
                    # add remain characters back to queue
                    next_word = curr_word[i:]
                    if not next_word:
                        return True
                    if next_word not in visited:
                        queue.append(next_word)
                        visited.add(next_word)
        return False        