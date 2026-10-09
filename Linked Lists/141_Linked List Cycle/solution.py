# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        else:
            fastPtr = head
            lowPtr = head

            while True:
                # Move the fast pointer two steps per slow-pointer step.
                i = 2
                while i > 0:
                    fastPtr = fastPtr.next
                    if fastPtr is None:
                        return False
                    # Meeting at the same node indicates a cycle.
                    if fastPtr is lowPtr:
                        return True
                    i = i - 1
                lowPtr = lowPtr.next

        