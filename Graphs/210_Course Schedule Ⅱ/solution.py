class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        gNode = {}
        inDegree = [0] * numCourses
        for item in prerequisites:
            inDegree[item[0]] = inDegree[item[0]] + 1
            if item[1] not in gNode:
                gNode[item[1]] = [item[0]]
            else:
                gNode[item[1]].append(item[0])

        ans = []
        ops = deque()

        for i in range(numCourses):
            if inDegree[i] == 0:
                ops.append(i)

        while len(ops) > 0:
            temOps = deque()
            while len(ops) > 0:
                temNode = ops.popleft()
                for item in gNode.get(temNode,[]):
                    inDegree[item] = inDegree[item] - 1
                    if inDegree[item] == 0:
                        temOps.append(item)
                ans.append(temNode)
            ops = temOps
        
        if len(ans) == numCourses:
            return ans
        else:
            return []

        