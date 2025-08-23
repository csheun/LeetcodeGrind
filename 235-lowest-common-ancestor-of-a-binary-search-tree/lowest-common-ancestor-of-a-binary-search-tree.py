# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = q_path = None
        def traverse(root, path):
            nonlocal p_path, q_path
            if root.val == p.val:
                p_path = path
            if root.val == q.val:
                q_path = path
            if p_path is not None and q_path is not None:
                return
            if root.left:
                traverse(root.left, path + [root.left])
            if root.right:
                traverse(root.right, path + [root.right])
        traverse(root, [root])
        # print(p)
        # print(p_path)
        # print(q_path)
        q_path = set([node.val for node in q_path])

        for i in range(len(p_path) - 1, -1 , -1):
            target = p_path[i].val
            if target in q_path:
                return p_path[i]

        return TreeNode(0)

        