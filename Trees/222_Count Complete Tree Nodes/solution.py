# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def FindRoute(idNum,lvlTotal):
            ans = []
            while idNum > 1:
                ans.append((idNum-lvlTotal+1)%2)
                idNum = idNum // 2
                lvlTotal = lvlTotal // 2
            return ans


        def Check(root,tarRoute):
            ptr = len(tarRoute) - 1
            while ptr >= 0:
                if tarRoute[ptr] == 0:
                    root = root.right
                else:
                    root = root.left
                ptr = ptr - 1
            if root is None:
                return False
            else:
                return True


        if root is None:
            return 0
        else:
            ptr = root
            leftH = 0
            while ptr is not None:
                ptr = ptr.left
                leftH = leftH + 1
            ptr = root
            rightH = 0
            while ptr is not None:
                ptr = ptr.right
                rightH = rightH + 1
            
            total = pow(2,rightH)

            if leftH == rightH:
                return total - 1
            else:
                left = 1
                right = total

                while right-left > 1:
                    mid = (left+right) // 2
                    midRoute = FindRoute(mid+total-1,total)
                    if Check(root,midRoute):
                        left = mid
                    else:
                        right = mid
                
                return total - 1 + left