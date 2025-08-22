# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def inorderTraverse(root, side) -> (int, int, bool):
            # print(f"curr_node: {root.val}")
            if root.left is None and root.right is None:
                # leaf node
                return root.val, root.val, True
            res = []
            if root.left:
                left_min, left_max, valid = inorderTraverse(root.left, 'left')
                if not valid or left_max >= root.val:
                    return None, None, False
                # print(f"left_max: {left_max}")
                res.append(left_max)
                res.append(left_min)
            if root.right:
                right_min, right_max, valid = inorderTraverse(root.right, 'right')
                if not valid or right_min <= root.val:
                    return None, None, False
                res.append(right_min)
                res.append(right_max)
                # print(f"right_min: {right_min}")
            res.append(root.val)
            return min(res), max(res), True

        _, _, valid = inorderTraverse(root, '')

        return valid
        