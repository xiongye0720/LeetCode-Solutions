class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        tripCnt = len(trips)
        tripDict = {}
        starts = set()
        for i in range(tripCnt):
            temRow = [trips[i][1], trips[i][2], trips[i][0]]
            starts.add(temRow[0])
            if temRow[0] in tripDict:
                tripDict[temRow[0]].append((temRow[1],temRow[2]))
            else:
                tripDict[temRow[0]] = [(temRow[1],temRow[2])]

        starts = list(starts)
        starts.sort()

        ops = []
        maxCnt = float('-inf')
        passCnt = 0

        for item in starts:
            while len(ops) > 0:
                if ops[0][0] > item:
                    break
                passCnt = passCnt - heapq.heappop(ops)[1]
            for term in tripDict[item]:
                passCnt = passCnt + term[1]
                heapq.heappush(ops,term)

            maxCnt = max(maxCnt,passCnt)

        return maxCnt <= capacity