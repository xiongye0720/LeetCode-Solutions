class Solution:
    def convert(self, s: str, numRows: int) -> str:
        tar = []
        right = len(s) - 1
        if numRows >= 2:
            step = 2*numRows - 2
            for i in range(numRows):
                if i==0 or i==numRows-1:
                    while i <= right:
                        tar.append(s[i])
                        i = i + step
                else:
                    count = 1
                    while i <= right:
                        tar.append(s[i])
                        i = (count*step) - (i%step)
                        if i > right:
                            break
                        tar.append(s[i])
                        i = (count*step - i) + count*step
                        count = count + 1
            tarS = ''.join(tar)
            return tarS
        else:
            return s