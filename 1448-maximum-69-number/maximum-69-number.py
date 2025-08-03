class Solution:
    def maximum69Number (self, num: int) -> int:
        num_lst = list(str(num))
        for i in range(len(num_lst)):
            if (num_lst[i] == '6'):
                num_lst[i] = '9'
                break
        return int(''.join(num_lst))
