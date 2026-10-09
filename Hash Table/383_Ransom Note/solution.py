class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alpha = [0] * 26
        # Count available letters in magazine.
        for char in magazine:
            alpha[ord(char)-ord('a')] = alpha[ord(char)-ord('a')] + 1
        # Consume one available letter for each character in ransomNote.
        for char in ransomNote:
            alpha[ord(char)-ord('a')] = alpha[ord(char)-ord('a')] - 1
            # A negative count means this letter is insufficient.
            if alpha[ord(char)-ord('a')] < 0:
                return False
        return True
