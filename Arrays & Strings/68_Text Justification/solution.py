class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        wordQue = deque()
        for item in words:
            wordQue.append(item)
        resWords = []
        
        while len(wordQue) > 0:
            rowLen = 0
            temRow = []
            while rowLen<=maxWidth and len(wordQue)>0:
                temWord = wordQue.popleft()
                if rowLen+len(temWord) > maxWidth:
                    wordQue.appendleft(temWord)
                    break
                else:
                    temRow.append(temWord)
                    rowLen = rowLen + len(temWord) + 1
            if len(wordQue) == 0:
                rowStr = ' '.join(temRow)
                rowStr = rowStr + (' ' * (maxWidth-len(rowStr)))
                resWords.append(rowStr)
            else:
                temLen = 0
                for item in temRow:
                    temLen = temLen + len(item)
                if len(temRow) == 1:
                    rowStr = temRow[0] + (' ' * (maxWidth-temLen))
                    resWords.append(rowStr)
                else:
                    quot = (maxWidth-temLen) // (len(temRow)-1)
                    rem = (maxWidth-temLen) % (len(temRow)-1)
                    if rem == 0:
                        sep = ' ' * quot
                        rowStr = sep.join(temRow)
                        resWords.append(rowStr)
                    else:
                        sep1 = ' ' * (quot+1)
                        sep2 = ' ' * quot
                        rowStr = ''
                        for i in range(rem):
                            rowStr = rowStr + temRow[i] + sep1
                        for i in range(rem,len(temRow)):
                            rowStr = rowStr + temRow[i] + sep2
                        rowStr = rowStr.rstrip(' ')
                        resWords.append(rowStr)
        
        return resWords
