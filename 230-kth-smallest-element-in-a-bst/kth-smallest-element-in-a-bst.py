# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal

        pos = [0]
        ans = [0]
        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            # print(root.val)
            pos[0] += 1
            if pos[0] == k:
                ans[0] = root.val
                return
            traverse(root.right)

        traverse(root)
        return ans[0]
        