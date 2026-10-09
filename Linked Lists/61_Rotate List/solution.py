# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        elif k == 0:
            return head
        else:
            ptr = head
            cnt = 0
            while True:
                cnt = cnt + 1
                if ptr.next is None:
                    break
                ptr = ptr.next

            k = k % cnt
            if k == 0:
                return head
            else:
                ptr.next = head
                k = cnt - k
                while k > 1:
                    head = head.next
                    k = k - 1
                nodeSt = head.next
                head.next = None

                return nodeSt
