class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Map each character in s to a character in t.
        mapDict = {}
        charSet = set()
        for i in range(len(s)):
            if s[i] in mapDict:
                # Repeated characters must keep the same mapping.
                if t[i] != mapDict[s[i]]:
                    return False
            else:
                # Different source characters cannot share a target character.
                if t[i] in charSet:
                    return False
                charSet.add(t[i])
                mapDict[s[i]] = t[i]
        
        return True
