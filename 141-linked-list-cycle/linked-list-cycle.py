# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_table = {}
        while head:
            if head.val not in hash_table:
                hash_table[head.val] = []
                hash_table[head.val].append(head)
            else:
                # loop through arr to see if same
                for node in hash_table[head.val]:
                    if head is node:
                        return True
                hash_table[head.val].append(head)
            head = head.next
        return False
            