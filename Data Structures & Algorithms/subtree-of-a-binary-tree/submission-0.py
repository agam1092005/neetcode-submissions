# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def equal(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False

            return equal(root.left, subRoot.left) and equal(root.right, subRoot.right)

        def help(root, subRoot):
            if not root:
                return False

            if equal(root, subRoot):
                return True

            return help(root.left, subRoot) or help(root.right, subRoot)

        return help(root, subRoot)
        