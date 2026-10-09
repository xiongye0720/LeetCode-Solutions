# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            ops = deque()
            ops.append(root)
            depth = 0

            # Each iteration processes one tree level.
            while len(ops) > 0:
                depth = depth + 1
                # Collect nodes for the next level.
                temOps = deque()
                while len(ops) > 0:
                    temNode = ops.popleft()
                    if temNode.left is not None:
                        temOps.append(temNode.left)
                    if temNode.right is not None:
                        temOps.append(temNode.right)
                ops = temOps
            
            return depth