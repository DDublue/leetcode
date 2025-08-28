from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # space: O(n)
        # time: O(n)

        def check_identical(root, subRoot):
            queue1 = deque([root])
            queue2 = deque([subRoot])
            while queue1 and queue2:
                node1 = queue1.popleft()
                node2 = queue2.popleft()
                
                if node1 and node2:
                    if node1.val != node2.val:
                        return False
                    queue1.append(node1.left)
                    queue1.append(node1.right)
                    queue2.append(node2.left)
                    queue2.append(node2.right)
                elif (not node1 and node2) or (node1 and not node2):
                    return False

            return queue1 == queue2

        main_queue = deque([root])
        potential_nodes = []
        while main_queue:
            node = main_queue.popleft()
            if node.val == subRoot.val:
                potential_nodes.append(node)
            if node.left:
                main_queue.append(node.left)
            if node.right:
                main_queue.append(node.right)

        if not potential_nodes:
            return False

        while potential_nodes:
            node = potential_nodes.pop()
            is_identical = check_identical(node, subRoot)
            if is_identical:
                return True
        
        return False
