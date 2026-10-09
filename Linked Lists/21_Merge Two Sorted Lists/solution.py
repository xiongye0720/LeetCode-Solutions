# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Use a dummy head to simplify linking nodes.
        nodeSt = ListNode()
        ptr = nodeSt

        # Append the smaller current node to the merged list.
        while (list1 is not None) and (list2 is not None):
            if list1.val <= list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
        
        # Attach the remaining nodes.
        if list1 is not None:
            ptr.next = list1
        if list2 is not None:
            ptr.next = list2
        
        return nodeSt.next
