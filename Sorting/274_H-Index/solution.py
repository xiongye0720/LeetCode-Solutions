class Solution:
    def hIndex(self, citations: List[int]) -> int:
        maxCite = 0
        for item in citations:
            maxCite = max(maxCite,item)
        
        upBound = max(maxCite,len(citations))

        citeDict = {}
        for item in citations:
            if item >= upBound:
                if upBound in citeDict:
                    citeDict[upBound] = citeDict[upBound] + 1
                else:
                    citeDict[upBound] = 1
            else:
                if item in citeDict:
                    citeDict[item] = citeDict[item] + 1
                else:
                    citeDict[item] = 1
            
        Total = 0
        while True:
            if upBound in citeDict:
                Total = Total + citeDict[upBound]
            if Total >= upBound:
                return upBound
            upBound = upBound - 1