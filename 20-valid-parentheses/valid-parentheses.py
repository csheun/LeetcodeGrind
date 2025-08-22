class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']
        matching_dict = {}
        for i in range(len(open_brackets)):
            matching_dict[close_brackets[i]] = open_brackets[i]
        open_brackets = set(open_brackets)
        close_brackets = set(close_brackets)

        stack = deque()
        for c in s:
            if c in open_brackets:
                stack.append(c)
            if c in close_brackets:
                if not stack:
                    return False
                target = stack.pop()
                if matching_dict[c] != target:
                    return False
        return not stack