class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Use the shortest string as the initial candidate.
        tarChar = strs[0]
        for item in strs:
            if len(item) < len(tarChar):
                tarChar = item
        
        for item in strs:
            # Find the matching prefix with the current string.
            ptr = 0
            while ptr<len(tarChar) and ptr<len(item):
                if tarChar[ptr] != item[ptr]:
                    break
                ptr = ptr + 1
            if ptr < len(tarChar):
                # Keep only the matching prefix.
                tarChar = tarChar[:ptr]
        
        return tarChar