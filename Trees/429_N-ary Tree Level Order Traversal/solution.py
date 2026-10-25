class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        levels = {1: []}
        stack = []

        node = root
        childCnt = len(node.children)
        levels[1].append(node.val)
        stack.append([node, 0, childCnt])

        while True:
            if stack[-1][1] == stack[-1][2]:
                stack.pop()
                if len(stack) > 0:
                    stack[-1][1] = stack[-1][1] + 1
                else:
                    break
            else:
                temNode = stack[-1][0].children[stack[-1][1]]
                temChildCnt = len(temNode.children)
                stack.append([temNode, 0, temChildCnt])
                if len(stack) in levels:
                    levels[len(stack)].append(temNode.val)
                else:
                    levels[len(stack)] = [temNode.val]

        ans = []
        for i in range(len(levels)):
            ans.append(levels[i + 1])
        return ans