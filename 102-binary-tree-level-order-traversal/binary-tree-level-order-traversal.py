# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder (self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        last, curr, output = [root], [], []
        while len (last) > 0:
            level = []
            for node in last:
                if not node: continue
                curr.extend ([ node.left, node.right, ])
                level.append (node.val)
            last, curr = curr, []
            if len (level) > 0: output.append (level)
        return output
