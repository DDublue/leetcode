from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # space: O(1)
        # time: O(n)

        # Delay forward pointer by n
        back = head
        front = head
        for i in range(n):
            front = front.next
        
        # 1 node
        if not front:
            return head.next

        # >1 nodes
        while front.next:
            front = front.next
            back = back.next
        
        # n'th node is the node pointed by 'back', so reconnect 'back's next 1 forward
        back.next = back.next.next

        return head
        
        