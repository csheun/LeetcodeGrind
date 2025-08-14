# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if not list1:
            return list2
        if not list2:
            return list1
        # both lists have smth
        res_node = None
        if list1.val <= list2.val:
            res_node = list1
            list1 = list1.next
        else:
            res_node = list2
            list2 = list2.next
        curr_node = res_node
        while list1 and list2:
            # print(f"list1_val: {list1.val}, list2_val: {list2.val}")
            if list1.val <= list2.val:
                curr_node.next = list1
                list1 = list1.next
            else:
                curr_node.next = list2
                list2 = list2.next
            curr_node = curr_node.next
        if list1:
            curr_node.next = list1
        else:
            curr_node.next = list2
        
        return res_node
        