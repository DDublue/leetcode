from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # space: O(1)
        # time: O(n)
        
        # Iterate through both lists until one of them ends; append the min of either current node each loop
        merged = ListNode()
        final = merged
        while list1 and list2:
            if list1.val < list2.val:
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            merged = merged.next
        
        merged.next = list1 if list1 else list2 # append the rest of the longer list to the merged list
        return final.next
