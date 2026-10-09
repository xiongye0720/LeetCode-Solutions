class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        ptrI = 0 
        initCol = 1
        while ptrI < row:
            ptrJ = 0
            while ptrJ < col:
                if matrix[ptrI][ptrJ] == 0:
                    if ptrJ == 0:
                        initCol = 0
                    else:
                        matrix[0][ptrJ] = 0
                    matrix[ptrI][0] = 0
                ptrJ = ptrJ + 1
            ptrI = ptrI + 1
        
        ptrI = row - 1
        while ptrI >= 0:
            ptrJ = col - 1
            while ptrJ >= 0:
                if ptrJ == 0:
                    if matrix[ptrI][0]==0 or initCol==0:
                        matrix[ptrI][ptrJ] = 0
                else:
                    if matrix[ptrI][0]==0 or matrix[0][ptrJ]==0:
                        matrix[ptrI][ptrJ] = 0
                ptrJ = ptrJ - 1
            ptrI = ptrI - 1