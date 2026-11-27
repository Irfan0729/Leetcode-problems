class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:

        if root is None:                    # base case: an empty tree stays empty
            return root

        self.invertTree(root.left)          # invert the left subtree
        self.invertTree(root.right)         # invert the right subtree
        root.right, root.left = root.left, root.right   # now swap this node's children
        return root
        