class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        pattern = {}
        length = len(beginWord)
        for item in wordList:
            for i in range(length):
                temStr = item[:i] + 'X' + item[i+1:]
                if temStr in pattern:
                    pattern[temStr].append(item)
                else:
                    pattern[temStr] = [item]
        
        ops = deque()
        cnt = 0
        visited = set()
        ops.append(beginWord)
        visited.add(beginWord)

        while len(ops) > 0:
            temOps = deque()
            cnt = cnt + 1
            while len(ops) > 0:
                temNode = ops.popleft()
                for i in range(length):
                    temStr = temNode[:i] + 'X' + temNode[i+1:]
                    if temStr in pattern:
                        for item in pattern[temStr]:
                            if item not in visited:
                                temOps.append(item)
                                visited.add(item)
                        del pattern[temStr]
            if endWord in visited:
                return cnt + 1
            ops = temOps

        return 0
                