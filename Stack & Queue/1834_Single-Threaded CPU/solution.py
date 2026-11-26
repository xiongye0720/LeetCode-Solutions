class task:
    def __init__(self,idx,duration,remTime):
        self.index = idx
        self.duration = duration
        self.remTime = remTime

    def __lt__(self, other):
        if self.duration == other.duration:
            return self.index < other.index
        else:
            return self.duration < other.duration


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        temRows = []
        for i in range(len(tasks)):
            temRows.append([tasks[i][0],i,tasks[i][1]])
        temRows.sort()

        pending = []
        now = float('-inf')
        ops = []
        runNode = None

        done = []
        for item in temRows:
            temRow = [item[1],item[2],item[2],item[0]]
            if now < int(temRow[3]):
                if now > float('-inf'):
                    for item in pending:
                        heapq.heappush(ops,item)

                    gapTime = int(temRow[3]) - now
                    while gapTime > 0 and (runNode is not None or len(ops)>0):
                        if runNode is None:
                            runNode = heapq.heappop(ops)
                        if runNode.remTime > gapTime:
                            runNode.remTime = runNode.remTime - gapTime
                            break
                        else:
                            temNode = runNode
                            runNode = None
                            done.append([temNode.index])
                            gapTime = gapTime - temNode.remTime
                pending = []
                pending.append(task(temRow[0],int(temRow[1]),int(temRow[2])))
                now = int(temRow[3])
            else:
                pending.append(task(temRow[0],int(temRow[1]),int(temRow[2])))

        for item in pending:
            heapq.heappush(ops,item)

        if runNode is not None:
            done.append([runNode.index])

        while len(ops) > 0:
            temNode = heapq.heappop(ops)
            done.append([temNode.index])

        ans = []
        for item in done:
            ans.append(item[0])
        return ans