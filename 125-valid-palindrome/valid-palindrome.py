class Solution:
    def isPalindrome(self, s: str) -> bool:
        # preprocess first
        str_list = []
        for i in range(len(s)):
            if s[i].isalnum():
                str_list.append(str(s[i]).lower())
        s = ''.join(str_list)
        r = len(s) - 1
        for i in range(len(s) // 2):
            if s[i] != s[r]:
                return False
            r -= 1
        return True
            
            
        