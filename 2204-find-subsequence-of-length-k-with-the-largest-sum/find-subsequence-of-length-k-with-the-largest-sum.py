class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        subseq = []

        for num in nums:
            if len(subseq) < k:
                subseq.append(num)
                continue
            min_num = min(subseq)
            if num > min_num:
                subseq.remove(min_num)
                subseq.append(num)
        
        return subseq