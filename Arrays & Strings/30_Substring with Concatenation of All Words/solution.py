class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        D = len(words[0])
        if len(s) < D*len(words):
            return []
        else:
            wordIdx = {}
            wordDict = {}
            count = 1
            for item in words:
                if item not in wordIdx:
                    wordIdx[item] = count
                    count = count + 1
                wordDict[wordIdx[item]] = wordDict.get(wordIdx[item],0) + 1
            idx = [-1] * (len(s)-D+1)
            for i in range(len(s)-D+1):
                temWord = s[i:i+D]
                if temWord in wordIdx:
                    idx[i] = wordIdx[temWord]

            resList =[]
                
            for i in range(D):
                diff = 0
                temDict = {}
                left = i
                right = i
                while left+len(words)*D <= len(s):
                    while right-left < len(words)*D:
                        if idx[right] != -1:
                            temDict[idx[right]] = temDict.get(idx[right],0) + 1
                            if temDict[idx[right]] == wordDict[idx[right]]:
                                diff = diff + 1
                            elif temDict[idx[right]] == wordDict[idx[right]] + 1:
                                diff = diff - 1
                        right = right + D
                    if diff == len(wordDict):
                        resList.append(left)
                    if idx[left] != -1:
                        temDict[idx[left]] = temDict[idx[left]] - 1
                        if temDict[idx[left]] == wordDict[idx[left]]:
                            diff = diff + 1
                        elif temDict[idx[left]] + 1 == wordDict[idx[left]]:
                            diff = diff - 1
                        if temDict[idx[left]] == 0:
                            del temDict[idx[left]]
                    left = left + D
            
            return resList
