class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastLen = 0
        left = 0
        while left < len(s):
            if s[left] == ' ':
                # Skip spaces between words or after the last word.
                left = left + 1
            else:
                right = left
                # Find the end of the current word.
                while right < len(s):
                    if s[right] == ' ':
                        break
                    right = right + 1
                # Keep the length of the most recently scanned word.
                lastLen = right - left
                left = right
        
        return lastLen
