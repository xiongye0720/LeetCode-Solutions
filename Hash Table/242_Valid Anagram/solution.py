class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            sDict = {}
            # Count each character in s.
            for char in s:
                sDict[char] = sDict.get(char,0) + 1
            for char in t:
                # Reject characters that are absent or already exhausted.
                if char not in sDict:
                    return False
                sDict[char] = sDict[char] - 1
                if sDict[char] == 0:
                    del sDict[char]
            # Equal lengths ensure all counts have been consumed.
            return True
        