# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        list_len = 0
        while curr:
            list_len += 1
            curr = curr.next
        if list_len <= 2:
            return head
        if list_len % 2 == 0:
            list_len = list_len // 2
        else:
            list_len = list_len // 2 + 1
        list1 = head
        list2 = None
        for i in range(list_len):
            if i == list_len - 1:
                list2 = list1.next
                list1.next = None
            else:
                list1 = list1.next
        list1 = head
        node = None
        while list2:
            temp = list2.next
            list2.next = node
            node = list2
            list2 = temp
        list2 = node
        head = list1
        res = list1
        temp = list1.next
        res.next = list2
        list1 = temp
        list2 = list2.next
        res = res.next
        for i in range(1, list_len):
            temp = list1.next
            res.next = list1
            list1 = temp
            res = res.next
            if list2:
                temp = list2.next
                res.next = list2
                list2 = temp
                res = res.next