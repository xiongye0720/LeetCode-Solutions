class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ops = deque()
        cnt = 0
        srch = ((-1,0),(0,-1),(0,1),(1,0))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt = cnt + 1
                    ops.append((i,j))
                    grid[i][j] = '0'

                    while len(ops) > 0:
                        temOps = deque()
                        while len(ops) > 0:
                            temNode = ops.popleft()
                            for item in srch:
                                dx = item[0] + temNode[0]
                                dy = item[1] + temNode[1]
                                if (dx>=0 and dx<m) and (dy>=0 and dy<n) and grid[dx][dy]=='1':
                                    grid[dx][dy] = '0'
                                    temOps.append((dx,dy))
                        ops = temOps
                    
        return cnt