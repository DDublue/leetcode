from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # space: O(n)
        # time: O(n)

        # Track seen nodes. If a current node already seen, then cycle exists.
        nodes = set()
        while head:
            if head in nodes:
                return True
            nodes.add(head)
            head = head.next
        return False
