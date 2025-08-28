from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # space: O(n)
        # time: O(n)
        
        if not head:
            return None

        current = head
        old_to_new = {}
        while current:
            # Map old to new node
            old_to_new[current] = Node(current.val)
            current = current.next

        # We now have all the nodes, so update the random
        current = head
        while current:
            old_to_new[current].next = old_to_new[current.next] if current.next else None
            old_to_new[current].random = old_to_new[current.random] if current.random else None
            current = current.next

        return old_to_new[head]
