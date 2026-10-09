# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def MergeLists(head,steps,length,total):
            initNode = ListNode()
            initNode.next = head
            ptrS = initNode
            temNode = ListNode()
            for i in range(steps):
                ptr1 = ptrS.next
                ptr2 = ptr1
                rem1 = length
                total = total - rem1
                for j in range(rem1):
                    ptr2 = ptr2.next
                ptrE = ptr2
                rem2 = min(length,total)
                total = total - rem2
                for j in range(rem2):
                    ptrE = ptrE.next
                
                temNode.next = None
                temPtr = temNode
                while rem1>0 or rem2>0:
                    if rem1==0 or (rem1>0 and rem2>0 and ptr2.val<ptr1.val):
                        temPtr.next = ptr2
                        temPtr = temPtr.next
                        ptr2 = ptr2.next
                        rem2 = rem2 - 1
                    else:
                        temPtr.next = ptr1
                        temPtr = temPtr.next
                        ptr1 = ptr1.next
                        rem1 = rem1 - 1
                ptrS.next = temNode.next
                temPtr.next = ptrE
                ptrS = temPtr
            return initNode.next


        if head is None:
            return None
        else:
            nums = 0
            ptr = head
            while ptr is not None:
                ptr = ptr.next
                nums = nums + 1

            length = 1
            total = nums
            while nums > 1:
                steps = (nums+1) // 2
                if nums%2 == 0:
                    head = MergeLists(head,steps,length,total)
                else:
                    head = MergeLists(head,steps-1,length,total)
                length = length * 2
                nums = steps

            return head  