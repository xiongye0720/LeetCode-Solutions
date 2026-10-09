# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Use a dummy head to simplify appending result nodes.
        res = ListNode()
        ptr = res
        quot = 0

        # Add digits from least significant to most significant.
        while (l1 is not None) or (l2 is not None):
            if l1 is None:
                temSum = l2.val + quot
            elif l2 is None:
                temSum = l1.val + quot
            else:
                temSum = l1.val + l2.val + quot
            # Store the current digit; quot carries into the next position.
            temNode = ListNode(temSum%10)
            ptr.next = temNode
            ptr = temNode
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            quot = temSum // 10
        
        # Append any carry remaining after both lists end.
        if quot != 0:
            temNode = ListNode(quot)
            ptr.next = temNode

        return res.next