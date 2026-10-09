# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None
        else:
            nodeDown = ListNode()
            nodeDown.next = head
            nodeUp = ListNode()
            ptrDown = nodeDown
            ptrUp = nodeUp
            while head is not None:
                if head.val >= x:
                    ptrDown.next = head.next
                    ptrUp.next = head
                    ptrUp = head
                    head = head.next
                else:
                    ptrDown = head
                    head = head.next
            
            ptrUp.next = None
            ptrDown.next = nodeUp.next

            return nodeDown.next
                    

        