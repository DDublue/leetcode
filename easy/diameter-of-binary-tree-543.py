from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # space: O(n)
        # time: O(n)

        self.max_diameter = 0

        # Need max heights to get diameter; takes account left + right height subtrees through any node
        # - improved from my initial solution of O(n^2)
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            self.max_diameter = max(self.max_diameter, left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.max_diameter
