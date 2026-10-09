# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        else:
            nodeSt = ListNode()
            nodeSt.next = head
            ptr = nodeSt
            ptr1 = head
            while ptr1 is not None:
                cnt = 1
                while ptr1.next is not None:
                    if ptr1.next.val != ptr1.val:
                        break
                    cnt = cnt + 1
                    ptr1 = ptr1.next
                if cnt == 1:
                    ptr = ptr1
                    ptr1 = ptr1.next
                else:
                    ptr1 = ptr1.next
                    ptr.next = ptr1
            
            return nodeSt.next


        