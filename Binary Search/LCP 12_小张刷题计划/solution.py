class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        times = time
        dayCnt = m

        maxTime = 0
        count = 0
        totalTime = 0

        for item in times:
            count = count + 1
            totalTime = totalTime + item
            if item > maxTime:
                maxTime = item

        if count <= dayCnt:
            return 0
        else:
            left = 0
            right = totalTime - maxTime

            while right - left > 1:
                mid = (left + right) // 2
                ptr = 0
                daysUsed = 0

                while ptr < len(times):
                    temPtr = ptr
                    temMax = 0
                    temSum = 0

                    while temPtr < len(times):
                        temSum = temSum + times[temPtr]
                        if times[temPtr] > temMax:
                            temMax = times[temPtr]

                        if temSum - temMax > mid:
                            break
                        temPtr = temPtr + 1

                    daysUsed = daysUsed + 1
                    ptr = temPtr

                if daysUsed > dayCnt:
                    left = mid
                else:
                    right = mid

            return right