class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def GCD(x,y):
            while y > 0:
                tem = x % y
                x = y
                y = tem
            return x


        maxQty = float('-inf')
        for i in range(len(points)):
            segs = {}
            temMax = 0
            for j in range(i+1,len(points)):
                A = points[j][1] - points[i][1]
                B = points[i][0] - points[j][0]
                C = points[i][1]*points[j][0] - points[i][0]*points[j][1]
                gcd = GCD(GCD(abs(A),abs(B)),abs(C))
                if (A<0) or (A==0 and B<0):
                    temSeg = (-1*(A//gcd),-1*(B//gcd),-1*(C//gcd))
                else:
                    temSeg = (A//gcd,B//gcd,C//gcd)
                
                segs[temSeg] = segs.get(temSeg,0) + 1
                temMax = max(temMax,segs[temSeg])
            maxQty = max(maxQty,temMax+1)
        
        return maxQty