class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            left = 0
            right = 0
            maxLen = 0
            charSet = set()
            while left < len(s):
                while right < len(s):
                    if s[right] in charSet:
                        break
                    charSet.add(s[right])
                    right = right + 1
                maxLen = max(maxLen,right-left)
                if right == len(s):
                    break
                charSet.remove(s[left])
                left = left + 1
            return maxLen