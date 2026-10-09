class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(pattern) != len(s):
            return False
        else:
            # Map each character to its word.
            rela = {}
            # Track words already assigned to a character.
            visit = set()

            for i in range(len(pattern)):
                if pattern[i] in rela:
                    # Repeated characters must match the same word.
                    if rela[pattern[i]] != s[i]:
                        return False
                else:
                    # Different characters cannot share the same word.
                    if s[i] in visit:
                        return False
                    rela[pattern[i]] = s[i]
                    visit.add(s[i])
            
            return True
        