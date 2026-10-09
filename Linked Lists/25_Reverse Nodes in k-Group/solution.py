# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        else:
            nodeSt = ListNode()
            nodeSt.next = head
            ptrL = nodeSt

            while True:
                ptrM = ptrL.next
                cnt = 0
                while ptrM is not None:
                    cnt = cnt + 1
                    if cnt == k:
                        break
                    ptrM = ptrM.next

                if cnt == k:
                    ptrM = ptrL.next
                    ptrN = ptrM.next
                    cnt = 2
                    while cnt <= k:
                        temMid = ptrN
                        ptrN = ptrN.next
                        temMid.next = ptrM
                        ptrM = temMid
                        cnt = cnt + 1
                    temPtr = ptrL.next
                    temPtr.next = ptrN
                    ptrL.next = ptrM
                    ptrL = temPtr
                else:
                    break
            
            return nodeSt.next


        