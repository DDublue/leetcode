from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # space: O(n)
        # time: O(n)
        
        order = []

        if not root:
            return order

        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()

            # Create new inner list if level for it doesn't exist at index (level - 1)
            if level > len(order):
                order.append([])
            order[level - 1].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return order
