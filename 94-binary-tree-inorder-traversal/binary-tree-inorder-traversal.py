# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal (self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return self._inorderTraversal_ (root, list ())

    def _inorderTraversal_ (self, root: Optional[TreeNode], order) -> List[int]:
        if not root: return order
        self._inorderTraversal_ (root.left, order)
        order.append (root.val)
        self._inorderTraversal_ (root.right, order)
        return order
