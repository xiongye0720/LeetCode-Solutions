# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def DFS(tNode,maxVal):
            if (tNode.left is None) and (tNode.right is None):
                dp = [tNode.val,float('-inf')]
                maxVal[0] = max(maxVal[0],dp[0],dp[1])
                return dp
            
            dp = [tNode.val,float('-inf')]
            if tNode.left is not None:
                dpLeft = DFS(tNode.left,maxVal)
                dp[0] = max(dp[0],tNode.val+dpLeft[0])
            if tNode.right is not None:
                dpRight = DFS(tNode.right,maxVal)
                dp[0] = max(dp[0],tNode.val+dpRight[0])
            if (tNode.left is not None) and (tNode.right is not None):
                dp[1] = tNode.val + dpLeft[0] + dpRight[0]
            
            maxVal[0] = max(maxVal[0],dp[0],dp[1])
            return dp


        maxVal = [float('-inf')]
        DFS(root,maxVal)

        return maxVal[0]
        