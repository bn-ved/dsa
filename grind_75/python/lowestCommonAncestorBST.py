class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        small = min(p.val, q.val)
        large = max(p.val, q.val)

        while root:
            if large < root.val:
                root = root.left
            if small > root.val:
                root = root.right
            else:
                return root
