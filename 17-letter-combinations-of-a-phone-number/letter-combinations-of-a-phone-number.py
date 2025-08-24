class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_letter_map = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        
        def backtrack(idx, arr):
            if idx == len(digits) - 1:
                res.append(''.join(arr))
            else:
                nxt_idx = idx + 1
                digit = int(digits[nxt_idx])
                letters = digit_letter_map[digit]
                for i in range(len(letters)):
                    char = letters[i]
                    # print(f"nxt_idx: {nxt_idx}, i: {i}, char: {char}")
                    backtrack(nxt_idx, arr + [char])
        
        res  = []
        backtrack(-1, [])

        return res