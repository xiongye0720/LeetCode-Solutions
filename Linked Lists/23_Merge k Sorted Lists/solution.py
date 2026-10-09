# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        else:
            ePtr = len(lists)

            while ePtr > 1:
                steps = (ePtr+1) // 2
                for i in range(steps):
                    if ePtr%2==1 and i==steps-1:
                        lists[i] = lists[2*i]
                    else:
                        ptr1 = lists[2*i]
                        ptr2 = lists[2*i+1]
                        initNode = ListNode()
                        ptr = initNode

                        while (ptr1 is not None) and (ptr2 is not None):
                            if ptr1.val <= ptr2.val:
                                ptr.next = ptr1
                                ptr1 = ptr1.next
                            else:
                                ptr.next = ptr2
                                ptr2 = ptr2.next
                            ptr = ptr.next
                        
                        if ptr1 is None:
                            ptr.next = ptr2
                        else:
                            ptr.next = ptr1
                        
                        lists[i] = initNode.next
                ePtr = steps

            return lists[0]   