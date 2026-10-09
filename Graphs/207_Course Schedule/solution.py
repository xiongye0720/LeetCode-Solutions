class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}
        inDegree = [0] * numCourses
        for item in prerequisites:
            if item[1] in courses:
                courses[item[1]].append(item[0])
            else:
                courses[item[1]] = [item[0]]
            inDegree[item[0]] = inDegree[item[0]] + 1

        ops = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                ops.append(i)
        
        cnt = 0

        while len(ops) > 0:
            temOps = deque()
            while len(ops) > 0:
                temNode = ops.popleft()
                cnt = cnt + 1
                for item in courses.get(temNode,[]):
                    inDegree[item] = inDegree[item] - 1
                    if inDegree[item] == 0:
                        temOps.append(item)
            ops = temOps
        
        if cnt == numCourses:
            return True
        else:
            return False
        