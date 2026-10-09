# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = []
        ops = deque()
        ops.append(root)
        father = {id(root):None}
        if (root is p) or (root is q):
            ans.append((root,0))
        
        height = 0

        while len(ops) > 0:
            temOps = deque()
            height = height + 1
            while len(ops) > 0:
                temNode = ops.popleft()
                if temNode.left is not None:
                    father[id(temNode.left)] = temNode
                    temOps.append(temNode.left)
                    if (temNode.left is p) or (temNode.left is q):
                        ans.append((temNode.left,height))
                if temNode.right is not None:
                    father[id(temNode.right)] = temNode
                    temOps.append(temNode.right)
                    if (temNode.right is p) or (temNode.right is q):
                        ans.append((temNode.right,height))
            ops = temOps
            if len(ans) == 2:
                break

        p = ans[0][0]
        q = ans[1][0]

        if ans[0][1] < ans[1][1]:
            steps = ans[1][1] - ans[0][1]
            if steps > 1: 
                while steps > 1:
                    q = father[id(q)]
                    steps = steps - 1
            if father[id(q)] is p:
                return p
            else:
                q = father[id(q)]

        while True:
            q = father[id(q)]
            p = father[id(p)]
            if p is q:
                return p
 