"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        ptrSt = root
        while ptrSt is not None:
            temNode = Node()
            temPtr = temNode
            while ptrSt is not None:
                if ptrSt.left is not None:
                    temPtr.next = ptrSt.left
                    temPtr = temPtr.next
                if ptrSt.right is not None:
                    temPtr.next = ptrSt.right
                    temPtr = temPtr.next
                ptrSt = ptrSt.next
            ptrSt = temNode.next
        
        return root
        