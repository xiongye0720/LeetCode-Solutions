class Solution:
    def reverseWords(self, s: str) -> str:
        def reverseStr(left,right,sList):
            while left < right:
                temChar = sList[left]
                sList[left] = sList[right]
                sList[right] = temChar
                left = left + 1
                right = right - 1

        sList = []
        for char in s:
            sList.append(char)
        left = 0
        right = 0
        endStr = len(sList) - 1

        while left <= endStr:
            if sList[left] == ' ':
                while right <= endStr:
                    if sList[right] != ' ':
                        break
                    right = right + 1
                
                if right > endStr:
                    endStr = left - 1
                else:
                    wordR = right
                    while wordR <= endStr:
                        if sList[wordR] == ' ':
                            break
                        wordR = wordR + 1
                    if left == 0:
                        for i in range(right,wordR):
                            sList[i-(right-left)] = sList[i]
                            sList[i] = ' '
                        left = left + (wordR - right)
                        right = wordR
                    elif right-left > 1:
                        for i in range(right,wordR):
                            sList[i-(right-left-1)] = sList[i]
                            sList[i] = ' '
                        left = left + (wordR - right) + 1
                        right = wordR
                    else:
                        left = wordR
                        right = wordR
            else:
                left = left + 1
                right = right + 1

        sList = sList[:endStr+1]

        left = 0
        reverseStr(left,endStr,sList)
        while True:
            if sList[left] != ' ':
                right = left
                while right <= endStr:
                    if sList[right] == ' ':
                        break
                    right = right + 1
                reverseStr(left,right-1,sList)
                if right > endStr:
                    break
                left = right + 1

        resStr = ''.join(sList)

        return resStr