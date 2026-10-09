# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is not None:
            def DFS(lastNode,currNode):
                leftChild = currNode.left
                rightChild = currNode.right

                lastNode[0].left = None
                lastNode[0].right = currNode
                lastNode[0] = currNode

                if leftChild is not None:
                    DFS(lastNode,leftChild)
                if rightChild is not None:
                    DFS(lastNode,rightChild)

            initNode = TreeNode()
            lastNode = [initNode]
            DFS(lastNode,root)


            