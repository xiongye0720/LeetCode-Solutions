class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        interv = intervals
        interv.sort()

        left = 0
        right = n
        while right-left > 1:
            mid = (left+right) // 2
            busy = []
            free = [0] * mid
            isOk = True

            for item in interv:
                now = item[0]
                while len(busy) > 0:
                    if busy[0][0] >= now:
                        break
                    temGroup = heapq.heappop(busy)
                    heapq.heappush(free,temGroup[1])
                if len(free) == 0:
                    isOk = False
                    break
                temGroup = heapq.heappop(free)
                heapq.heappush(busy,(item[1],temGroup+1))

            if isOk:
                right = mid
            else:
                left = mid

        return right