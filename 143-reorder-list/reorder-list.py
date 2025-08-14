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
        # print(f"start: {list_len}")
        if list_len <= 2:
            return head
        if list_len % 2 == 0:
            list_len = list_len // 2
        else:
            list_len = list_len // 2 + 1
        list1 = head
        list2 = None
        # print(f"list_len: {list_len}")
        for i in range(list_len):
            if i == list_len - 1:
                list2 = list1.next
                list1.next = None
            else:
                list1 = list1.next
        list1 = head
        list1Print = list1
        # print("Printing list1")
        # while list1Print:
        #     print(list1Print.val)
        #     list1Print = list1Print.next
        
        # list1Print = list2
        # print("Printing list2")
        # while list1Print:
        #     print(list1Print.val)
        #     list1Print = list1Print.next
        # reverse list 2
        node = None
        while list2:
            temp = list2.next
            list2.next = node
            node = list2
            list2 = temp
        reversed_list2 = node
        list2 = reversed_list2
        output = list1
        res = list1
        temp = list1.next
        res.next = list2
        list1 = temp
        list2 = list2.next
        res = res.next
        # print(f"start: res.val: {res.val}")
        for i in range(1, list_len):
            # print(f"start of i: {i}")
            # # add list 1 add list 2
            # # print(f"i: {i}, list1: {list1.val}, list2: {list2.val}")
            temp = list1.next
            res.next = list1
            list1 = temp
            res = res.next
            if list2:
                temp = list2.next
                res.next = list2
                list2 = temp
                res = res.next
        # print(output)
        # while output:
        #     print(output.val)
        #     output = output.next
        head = output