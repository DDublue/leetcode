from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # space: O(n)
        # time: O(n)

        if not head or not head.next:
            return head

        # Fill stack
        stack = []
        temp = head
        while temp:
            stack.append(temp)
            temp = temp.next

        # Pop and append to reverse the linked list
        head = stack.pop()
        final = head
        while stack:
            head.next = stack.pop()
            head = head.next

        # Last node may still be pointing to a non-null node
        head.next = None

        return final
