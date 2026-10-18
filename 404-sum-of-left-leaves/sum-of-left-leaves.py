# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        # 
        sum = 0
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            if curr.right:
                q.append(curr.right)
            if curr.left and not curr.left.left and not curr.left.right:
                sum += curr.left.val
                continue
            if curr.left:
                q.append(curr.left)
        return sum
        