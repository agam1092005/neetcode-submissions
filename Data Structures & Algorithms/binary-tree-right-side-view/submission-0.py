# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []

        q = deque([root])
        while q:
            length = len(q)
            right_side = None

            for i in range(length):
                node = q.popleft()
                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)

            if right_side:
                right_view.append(right_side.val)
            
        return right_view