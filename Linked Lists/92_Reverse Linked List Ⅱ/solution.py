# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        else:
            initNd = ListNode()
            initNd.next = head
            ptr = initNd
            cnt = 1
            while cnt < left:
                ptr = ptr.next
                cnt = cnt + 1
            ptrSt = ptr
            ptr = ptr.next
            ptr1 = ptr.next
            cnt = 2
            while cnt <= right-left+1:
                temPtr = ptr1
                ptr1 = ptr1.next
                temPtr.next = ptr
                ptr = temPtr
                cnt = cnt + 1

            ptrSt.next.next = ptr1
            ptrSt.next = ptr

            return initNd.next



