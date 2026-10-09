# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        else:
            res = []
            ops = deque()
            ops.append(root)

            while len(ops) > 0:
                # Keep the next level separate from the current level.
                temOps = deque()
                while len(ops) > 0:
                    temNode = ops.popleft()
                    # The last node in this level is visible from the right.
                    if len(ops) == 0:
                        res.append(temNode.val)
                    # Preserve left-to-right order for the next level.
                    if temNode.left is not None:
                        temOps.append(temNode.left)
                    if temNode.right is not None:
                        temOps.append(temNode.right)
                ops = temOps
            
            return res