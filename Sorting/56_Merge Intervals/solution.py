class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for item in intervals:
            if len(res) == 0:
                res.append(item)
            else:
                if item[0] > res[-1][1]:
                    res.append(item)
                else:
                    res[-1][1] = max(item[1],res[-1][1])
        
        return res
        