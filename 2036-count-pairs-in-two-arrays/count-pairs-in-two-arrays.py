class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:

        # # brute force

        # n = len(nums1)
        # count = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums1[i] + nums1[j] > nums2[i] + nums2[j]:
        #             count += 1
        
        # return count

        '''
        rearranging nums1[i] - nums1[j] > nums2[i] - nums2[j]:
        (nums1[i] - nums2[i]) + (nums1[j] - nums2[j]) > 0 

        sort and use two pointers
        '''

        diff = [nums1[i] - nums2[i] for i in range(len(nums1))]
        diff.sort()

        count = 0
        r = len(nums1) - 1
        l = 0
        while l < r:
            if diff[l] + diff[r] > 0:
                count += (r - l)
                r -= 1
            else:
                l += 1
        return count