# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(tuple([root, 1]))
        res = []
        curr_level = 1 
        level_arr = []
        while queue:
            node, level = queue.popleft()
            if not node:
                continue
            if level == curr_level:
                level_arr.append(node.val)
            else:
                res.append(level_arr)
                curr_level = level
                level_arr = [node.val]
            queue.append(tuple([node.left, level + 1]))
            queue.append(tuple([node.right, level + 1]))
        if level_arr:
            res.append(level_arr)

        return res
        