# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def DFS(root,nums,total):
            nums[0] = nums[0]*10 + root.val
            if (root.left is None) and (root.right is None):
                total[0] = total[0] + nums[0]
                nums[0] = (nums[0]-root.val) // 10
                return
            if root.left is not None:
                DFS(root.left,nums,total)
            if root.right is not None:
                DFS(root.right,nums,total)
            nums[0] = (nums[0]-root.val) // 10
            return

        nums = [0]
        total = [0]
        DFS(root,nums,total)

        return total[0]