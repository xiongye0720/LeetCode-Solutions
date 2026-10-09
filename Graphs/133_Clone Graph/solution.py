"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        else:
            ops = deque()
            gNode = {id(node):Node(node.val,[])}
            ops.append(node)

            while len(ops) > 0:
                temOps = deque()
                while len(ops) > 0:
                    temNode = ops.popleft()
                    cloneN = gNode[id(temNode)]
                    for item in temNode.neighbors:
                        if id(item) not in gNode:
                            temCloneN = Node(item.val,[]) 
                            gNode[id(item)] = temCloneN
                            cloneN.neighbors.append(temCloneN)
                            temOps.append(item)
                        else:
                            cloneN.neighbors.append(gNode[id(item)])
                ops = temOps
            
            return gNode[id(node)]
        