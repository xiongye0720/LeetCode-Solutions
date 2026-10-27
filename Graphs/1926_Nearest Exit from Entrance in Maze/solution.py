class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        nRow = len(maze)
        nCol = len(maze[0])
        mat = maze
        visit = []

        for i in range(nRow):
            visit.append(['n'] * nCol)

        ops = deque()
        for i in range(nRow):
            for j in range(nCol):
                if (i, j) == (entrance[0], entrance[1]):
                    visit[i][j] = 'y'
                    ops.append([(i, j), 0])
                if mat[i][j] == '+':
                    visit[i][j] = 'y'

        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        notFound = True

        while len(ops) > 0 and notFound:
            temNodes = {}

            while len(ops) > 0:
                temNode = ops.popleft()

                nextNodes = [(temNode[0][0]+dirs[0][0],temNode[0][1]+dirs[0][1]),(temNode[0][0]+dirs[1][0],temNode[0][1]+dirs[1][1]),(temNode[0][0]+dirs[2][0],temNode[0][1]+dirs[2][1]),(temNode[0][0]+dirs[3][0],temNode[0][1]+dirs[3][1])]

                for item in nextNodes:
                    if (item[0]>=0 and item[0]<nRow) and (item[1]>=0 and item[1]<nCol) and visit[item[0]][item[1]]=='n':
                        if (item[0],item[1]) not in temNodes:
                            temNodes[(item[0],item[1])] = temNode[1]

            for key in temNodes:
                if key[0] == 0 or key[0] == nRow - 1 or key[1] == 0 or key[1] == nCol - 1:
                    ans = temNodes[key] + 1
                    notFound = False
                ops.append([key, temNodes[key] + 1])
                visit[key[0]][key[1]] = 'y'

        if notFound:
            return -1
        else:
            return ans