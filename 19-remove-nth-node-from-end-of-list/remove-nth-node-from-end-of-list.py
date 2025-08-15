# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # general idea: two pointers, one will move as per normal the other one will
        # move when it nth step after the first one
        
        # when len of linkedlist is 1, then it can only remove itself
        if not head.next:
            return head.next
        

        fast = head
        slow = head
        prev = None
        count = 0

        while fast:
            fast = fast.next
            if (count >= n):
                prev = slow
                slow = slow.next
            count += 1
        
        # end of loop: slow will be pointing to the node that is supposed to be removed
        # and prev will the node before slow

        if not prev:
            head = head.next
        else:
            prev.next = slow.next
        return head
        
        
        