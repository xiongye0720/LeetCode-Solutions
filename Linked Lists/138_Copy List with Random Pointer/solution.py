"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        else:
            res = head
            while res is not None:
                temNode = Node(res.val)
                temNode.next = res.next
                res.next = temNode
                res = temNode.next
            res = head
            while res is not None:
                if res.random is not None:
                    res.next.random = res.random.next
                res = res.next.next
            res = head.next
            ptr = res
            while ptr.next is not None:
                head.next = ptr.next
                head = head.next
                ptr.next = head.next
                ptr = ptr.next
            head.next = None
            
            return res