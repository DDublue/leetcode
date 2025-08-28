from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def get_height(self, root):
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # space: O(n)
        # time: O(n)

        if not root:
            return True

        queue = [root]
        while queue:
            node = queue.pop(0)
            left_tree = node.left if node.left else None
            right_tree = node.right if node.right else None

            left_height = self.get_height(left_tree)
            right_height = self.get_height(right_tree)

            if abs(left_height - right_height) > 1:
                return False

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return True
