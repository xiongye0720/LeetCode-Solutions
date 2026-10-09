class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        charDict = {}
        for i in range(3):
            for j in range(3):
                sqList = [0] * 9
                for k in range(3):
                    for l in range(3):
                        dx = i*3 + k
                        dy = j*3 + l
                        if board[dx][dy] != '.':
                            num = int(board[dx][dy])
                            if num in charDict:
                                if (dx in charDict[num][0]) or (dy in charDict[num][1]):
                                    return False
                                else:
                                    charDict[num][0].add(dx)
                                    charDict[num][1].add(dy)
                            else:
                                charDict[num] = [{dx},{dy}]
                            
                            if sqList[num-1] == 0:
                                sqList[num-1] = 1
                            else:
                                return False
        return True