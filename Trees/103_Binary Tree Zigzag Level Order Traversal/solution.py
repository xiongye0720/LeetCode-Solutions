# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        else:
            ops = deque()
            ops.append(root)
            res = []
            isOdd = True

            while len(ops) > 0:
                temOps = deque()
                temRow = []
                if isOdd:
                    while len(ops) > 0:
                        temNode = ops.popleft()
                        temRow.append(temNode.val)
                        if temNode.left is not None:
                            temOps.appendleft(temNode.left)
                        if temNode.right is not None:
                            temOps.appendleft(temNode.right)
                else:
                    while len(ops) > 0:
                        temNode = ops.popleft()
                        temRow.append(temNode.val)
                        if temNode.right is not None:
                            temOps.appendleft(temNode.right)
                        if temNode.left is not None:
                            temOps.appendleft(temNode.left)
                res.append(temRow)
                isOdd = not isOdd
                ops = temOps
            
            return res