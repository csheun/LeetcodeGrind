# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        arr = []

        while head:
            arr.append(head.val)
            head = head.next
        
        res = 0
        val = 1

        for i in range(len(arr) - 1, -1 , -1):
            res += arr[i] * val
            val *= 2
        
        return res