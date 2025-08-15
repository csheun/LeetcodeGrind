# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def getNumber(node: Optional[ListNode]) -> int:
            res = 0
            idx = 0
            while node:
                res += node.val * (10 ** idx)
                idx += 1
                node = node.next
            return res

        res_val = getNumber(l1) + getNumber(l2)
        if res_val == 0:
            return ListNode(res_val)
        
        dummy_node = ListNode()
        head = dummy_node

        while res_val != 0:
            head.next = ListNode(res_val % 10)
            head = head.next
            res_val //= 10

        return dummy_node.next