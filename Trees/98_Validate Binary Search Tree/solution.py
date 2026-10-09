# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def DFS(isOK,currNode,valRan):
            if currNode.val<=valRan[0] or currNode.val>=valRan[1]:
                isOK[0] = False
                return

            if currNode.left is not None:
                DFS(isOK,currNode.left,(valRan[0],currNode.val))
                if not isOK[0]:
                    return
            if currNode.right is not None:
                DFS(isOK,currNode.right,(currNode.val,valRan[1]))


        isOK = [True]
        valRan = (float('-inf'),float('inf'))
        DFS(isOK,root,valRan)

        return isOK[0]
        