class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for item in strs:
            alpha = [0] * 26
            for char in item:
                alpha[ord(char)-ord('a')] = alpha[ord(char)-ord('a')] + 1
            alpha = tuple(alpha)
            if alpha in words:
                words[alpha].append(item)
            else:
                words[alpha] = [item]
        
        res = []
        for key in words:
            res.append(words[key])

        return res
        