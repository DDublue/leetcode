from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # space: O(n)
        # time: O(n)

        def dfs(root, currentSum):
            if not root:
                return False
            
            currentSum += root.val

            # Reached a leaf
            if not root.left and not root.right:
                return currentSum == targetSum

            # Children still exists
            left = dfs(root.left, currentSum)
            right = dfs(root.right, currentSum)

            return left or right

        return dfs(root, 0)
