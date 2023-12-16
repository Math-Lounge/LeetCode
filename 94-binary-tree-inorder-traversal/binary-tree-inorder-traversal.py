# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal (self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return self._inorderTraversalIterative_ (root)
        return self._inorderTraversalRecurse_ (root, list ())

    def _inorderTraversalRecurse_ (self, root: Optional[TreeNode], order) -> List[int]:
        if not root: return order
        self._inorderTraversalRecurse_ (root.left, order)
        order.append (root.val)
        self._inorderTraversalRecurse_ (root.right, order)
        return order

    def _inorderTraversalIterative_ (self, root: Optional[TreeNode]) -> List[int]:
        order, stack = [], []
        while (len (stack) > 0) or (root is not None):
            while (root is not None):
                stack.append (root)
                root = root.left
            root = stack.pop ()
            order.append (root.val)
            root = root.right
        return order
