from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # space: O(n)
        # time: O(n)

        if not p and not q:
            return True
        elif not p or not q:
            return False

        # Comparing and appending nodes
        p_queue = deque([p])
        q_queue = deque([q])
        while p_queue and q_queue:
            p_node = p_queue.popleft()
            q_node = q_queue.popleft()

            if p_node and q_node:
                if (p_node.val != q_node.val):
                    return False
                p_queue.append(p_node.left)
                p_queue.append(p_node.right)
                q_queue.append(q_node.left)
                q_queue.append(q_node.right)
            elif (not p_node and q_node) or (p_node and not q_node):
                return False

        return p_queue == q_queue
