class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ops = points[0]
        count = 1
        for i in range(1,len(points)):
            if points[i][0] > ops[1]:
                count = count + 1
                ops = points[i]
            else:
                left = max(ops[0],points[i][0])
                right = min(ops[1],points[i][1])
                ops = [left,right]
        
        return count