class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        isValid = True
        while left < right:
            # Skip non-alphanumeric characters from the left.
            while left < right:
                if (s[left]>='a' and s[left]<='z') or (s[left]>='A' and s[left]<='Z') or (s[left]>='0' and s[left]<='9'):
                    break
                left = left + 1
            if left == right:
                break
            # Skip non-alphanumeric characters from the right.
            while right > left:
                if (s[right]>='a' and s[right]<='z') or (s[right]>='A' and s[right]<='Z') or (s[right]>='0' and s[right]<='9'):
                    break
                right = right - 1
            if left == right:
                break

            # Normalize case before comparing.
            temL = s[left].lower()
            temR = s[right].lower()

            if temL == temR:
                left = left + 1
                right = right - 1
            else:
                # A mismatch means the string is not a palindrome.
                isValid = False
                break
        
        return isValid
