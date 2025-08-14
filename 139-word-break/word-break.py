from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # # BFS method (passed)
        # # should acutally use DFS instead
        # word_set = set()
        # max_word_len = len(wordDict[0])
        # min_word_len = len(wordDict[0])
        # for word in wordDict:
        #     word_set.add(word)
        #     max_word_len = max(max_word_len, len(word))
        #     min_word_len = min(min_word_len, len(word))
        # queue = deque()
        # queue.append(s)
        # visited = set()
        # visited.add(s)
        # while queue:
        #     curr_word = queue.popleft()
        #     for i in range(min_word_len, max_word_len +1):
        #         target = curr_word[:i]
        #         if target in word_set:
        #             # add remain characters back to queue
        #             next_word = curr_word[i:]
        #             if not next_word:
        #                 return True
        #             if next_word not in visited:
        #                 queue.append(next_word)
        #                 visited.add(next_word)
        # return False        

        '''
        dp solution: 
        1) dp[] of size n + 1
        2) dp[i] = True if there string[:m] can be segmented
        3) how to decide set dp[i]: 1) need to iteratively go back and check
        if word is in dict 2) then check the dp[i - len(word)] is true
        '''

        word_set = set()
        max_len = min_len = len(wordDict[0])
        for word in wordDict:
            word_set.add(word)
            max_len = max(max_len, len(word))
            min_len = min(min_len, len(word))
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(max(-1, i - min_len), max(-1, i - max_len - 1), -1):
                curr_word = s[j:i]
                if (dp[j] and curr_word in word_set):
                    dp[i] = True
                    break
        
        return dp[len(s)]
        