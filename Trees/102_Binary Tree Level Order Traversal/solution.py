# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        else:
            ops = deque()
            ops.append(root)
            res = []

            # Process one level at a time.
            while len(ops) > 0:
                # Collect the next level separately.
                temOps = deque()
                temRes = []
                while len(ops) > 0:
                    temNode = ops.popleft()
                    temRes.append(temNode.val)
                    # Enqueue children from left to right.
                    if temNode.left is not None:
                        temOps.append(temNode.left)
                    if temNode.right is not None:
                        temOps.append(temNode.right)
                res.append(temRes)
                ops = temOps
            
            return res
        