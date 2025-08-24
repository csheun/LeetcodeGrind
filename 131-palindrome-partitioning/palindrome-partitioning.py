class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(s: str) -> bool:
            i = 0
            j = len(s) - 1

            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        palindrome_dict = {}
        res = []
        # generate all possible partition
        def backtrack(idx, length, arr):
            if length == 0:
                res.append(arr)
            else:
                for i in range(1, length + 1):
                    # add the
                    substring = s[idx:idx + i]
                    if substring not in palindrome_dict:
                        palindrome_dict[substring] = isPalindrome(substring)  
                    palindrome_check = palindrome_dict[substring]
                    if palindrome_check:
                        backtrack(idx + i, length - i, arr + [substring])
        
        backtrack(0, len(s), [])

        return res
        