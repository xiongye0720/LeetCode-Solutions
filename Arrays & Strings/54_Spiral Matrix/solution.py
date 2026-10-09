class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        col = len(matrix[0])
        row = len(matrix)
        Pt = deque()
        Pt.append((0,0))
        dirStr = 'right'

        resList = []
        while True:
            temNode = Pt.popleft()
            if temNode[0]==row or temNode[1]==-1 or (matrix[temNode[0]][temNode[1]] is None):
                break
            resList.append(matrix[temNode[0]][temNode[1]])
            matrix[temNode[0]][temNode[1]] = None

            if dirStr == 'right':
                if temNode[1]+1==col or (matrix[temNode[0]][temNode[1]+1] is None):
                    dirStr = 'down'
                    Pt.append((temNode[0]+1,temNode[1]))
                else:
                    Pt.append((temNode[0],temNode[1]+1))
            elif dirStr == 'down':
                if temNode[0]+1==row or (matrix[temNode[0]+1][temNode[1]] is None):
                    dirStr = 'left'
                    Pt.append((temNode[0],temNode[1]-1))
                else:
                    Pt.append((temNode[0]+1,temNode[1]))
            elif dirStr == 'left':
                if temNode[1]-1==-1 or (matrix[temNode[0]][temNode[1]-1] is None):
                    dirStr = 'up'
                    Pt.append((temNode[0]-1,temNode[1]))
                else:
                    Pt.append((temNode[0],temNode[1]-1))
            elif dirStr == 'up':
                if temNode[0]-1==-1 or (matrix[temNode[0]-1][temNode[1]] is None):
                    dirStr = 'right'
                    Pt.append((temNode[0],temNode[1]+1))
                else:
                    Pt.append((temNode[0]-1,temNode[1]))
        
        return resList