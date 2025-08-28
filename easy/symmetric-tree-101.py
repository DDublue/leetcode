from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # space: O(n)
        # time: O(n)

        if not root:
            return True
        
        # Similar to "same binary tree" question but other tree is "reversed"
        left_queue = deque([root.left])
        right_queue = deque([root.right])
        while left_queue and right_queue:
            left_node = left_queue.popleft()
            right_node = right_queue.popleft()

            if left_node and right_node:
                if left_node.val != right_node.val:
                    return False
                left_queue.append(left_node.left)
                left_queue.append(left_node.right)
                right_queue.append(right_node.right) # here is the difference
                right_queue.append(right_node.left)
            elif (not left_node and right_node) or (left_node and not right_node):
                return False

        return left_queue == right_queue
