class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def BFS(board,ptx,pty):
            ops = deque()
            ops.append((ptx,pty))
            board[ptx][pty] = None

            while len(ops) > 0:
                temOps = deque()
                while len(ops) > 0:
                    temNode = ops.popleft()
                    for item in srch:
                        dx = temNode[0] + item[0]
                        dy = temNode[1] + item[1]
                        if (dx>=0 and dx<m) and (dy>=0 and dy<n) and board[dx][dy]=='O':
                            temOps.append((dx,dy))
                            board[dx][dy] = None
                ops = temOps

        m = len(board)
        n = len(board[0])
        srch = ((-1,0),(0,-1),(0,1),(1,0))

        for j in range(n):
            if board[0][j] == 'O':
                BFS(board,0,j)
            if board[m-1][j] == 'O':
                BFS(board,m-1,j)
        for i in range(m):
            if board[i][0] == 'O':
                BFS(board,i,0)
            if board[i][n-1] == 'O':
                BFS(board,i,n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] is None:
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        