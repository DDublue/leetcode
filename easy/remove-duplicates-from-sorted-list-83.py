from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # space: O(1)
        # time: O(n)
        
        if not head:
            return head

        current_node = head
        current_number = head.val
        while current_node.next:
            if current_node.next.val == current_number: # keep checking if next is dupe as we reassign 'next'
                current_node.next = current_node.next.next
            else: # no dupe, so we can move to the next node
                current_node = current_node.next
                current_number = current_node.val

        return head
