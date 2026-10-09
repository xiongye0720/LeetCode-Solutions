class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDict = {}
        for char in t:
            tDict[char] = tDict.get(char,0) + 1

        diff = 0
        sDict = {}
        left = 0
        right = 0
        ansRange = None
        minLen = float('inf')

        while left < len(s):
            while right<len(s) and diff<len(tDict):
                if s[right] in tDict:
                    sDict[s[right]] = sDict.get(s[right],0) + 1
                    if sDict[s[right]] == tDict[s[right]]:
                        diff = diff + 1
                right = right + 1
            
            if diff < len(tDict):
                break
            
            if right-left < minLen:
                ansRange = (left,right)
                minLen = right - left
            
            if s[left] in tDict:
                sDict[s[left]] = sDict[s[left]] - 1
                if sDict[s[left]] == tDict[s[left]] - 1:
                    diff = diff - 1
                if sDict[s[left]] == 0:
                    del sDict[s[left]]
            
            left = left + 1

        if minLen == float('inf'):
            return ''
        else:
            return s[ansRange[0]:ansRange[1]]