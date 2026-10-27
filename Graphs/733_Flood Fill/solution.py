class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        matInfo = [len(image),len(image[0])]
        mat = image
        init = [(sr,sc)]
        oldColor = mat[sr][sc]

        dirs = ((-1,0),(0,-1),(0,1),(1,0))

        for item in init:
            # Track visits separately, even when color equals oldColor.
            visit = []
            for i in range(matInfo[0]):
                visit.append([0] * matInfo[1])
            ops = deque()
            ops.append(item)
            visit[item[0]][item[1]] = 1

            # Explore the connected region level by level.
            while len(ops) > 0:
                temOps = deque()
                while len(ops) > 0:
                    temNode = ops.popleft()
                    mat[temNode[0]][temNode[1]] = color
                    for step in dirs:
                        row = step[0] + temNode[0]
                        col = step[1] + temNode[1]
                        if (row>=0 and row<matInfo[0]) and (col>=0 and col<matInfo[1]) and mat[row][col]==oldColor and visit[row][col]==0:
                            temOps.append((row,col))
                            # Mark on enqueue to prevent duplicate entries.
                            visit[row][col] = 1
                ops =temOps

        return mat