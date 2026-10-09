class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ptr = 0
        res = []
        isInsert = False

        while ptr < len(intervals):
            if newInterval[1] < intervals[ptr][0]:
                res.append(newInterval)
                isInsert = True
                break
            elif intervals[ptr][1] < newInterval[0]:
                res.append(intervals[ptr])
                ptr = ptr + 1
            else:
                temIntv = intervals[ptr]
                left = min(temIntv[0],newInterval[0])
                right = max(temIntv[1],newInterval[1])
                res.append([left,right])
                isInsert = True
                ptr = ptr + 1
                break
        
        if isInsert:
            while ptr < len(intervals):
                temIntv = intervals[ptr]
                if res[-1][1] >= temIntv[0]:
                    res[-1][1] = max(res[-1][1],temIntv[1])
                else:
                    res.append(temIntv)
                ptr = ptr + 1
        else:
            res.append(newInterval)

        return res
