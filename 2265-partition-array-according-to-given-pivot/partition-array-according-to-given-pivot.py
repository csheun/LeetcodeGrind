class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        # 
        s_arr = []
        m_arr = []
        b_arr = []
        for num in nums:
            if num < pivot:
                s_arr.append(num)
            elif num > pivot:
                b_arr.append(num)
            else:
                m_arr.append(num)
        s_arr.extend(m_arr)
        s_arr.extend(b_arr)
        for i in range(len(s_arr)):
            nums[i] = s_arr[i]
        
        return nums