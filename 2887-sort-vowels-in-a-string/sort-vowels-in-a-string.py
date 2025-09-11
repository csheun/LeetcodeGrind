class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        arr = []
        for c in s:
            if c.lower() in vowels:
                arr.append(c)
        arr.sort()
        res = []
        j = 0
        for i in range(len(s)):
            if s[i].lower() in vowels:
                res.append(arr[j])
                j += 1
            else:
                res.append(s[i])
        
        return ''.join(res)
        