from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # space: O(1)
        # time: O(n)

        # Fast moves 2x more than slow, thus guarantees a middle find.
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
