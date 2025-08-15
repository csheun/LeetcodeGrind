"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # intuition: create the basic linked list first, hashmap old_to_new use the old node
        # as key and the new node as value
        # second loop then update the random and next
        if not head:
            return None
        
        hash_map = {}
        # hash_map[None] = None
        curr = head
        while curr:
            hash_map[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            # using hash_map.get() instead of [] to handle none cases
            hash_map[curr].next = hash_map.get(curr.next)
            hash_map[curr].random = hash_map.get(curr.random)
            curr = curr.next
        return hash_map[head]
