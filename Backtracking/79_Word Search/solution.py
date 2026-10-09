class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def DFS(x,y,lvl,board,ans):
            board[x][y] = None

            if lvl == maxLvl:
                ans[0] = True
                board[x][y] = word[lvl-1]
                return
            for item in srch:
                dx = item[0] + x
                dy = item[1] + y
                if (dx>=0 and dx<m) and (dy>=0 and dy<n) and board[dx][dy]==word[lvl]:
                    DFS(dx,dy,lvl+1,board,ans)
                    if ans[0]:
                        board[x][y] = word[lvl-1]
                        return
            board[x][y] = word[lvl-1]

        
        maxLvl = len(word)
        ans = [False]
        m = len(board)
        n = len(board[0])
        srch = ((-1,0),(0,-1),(0,1),(1,0))

        if word[0] != word[-1]:
            cntS = 0
            cntE = 0
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        cntS = cntS + 1
                    elif board[i][j] == word[-1]:
                        cntE = cntE + 1
            if cntE < cntS:
                word = word[::-1]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    DFS(i,j,1,board,ans)
                    if ans[0]:
                        break
            if ans[0]:
                break
        
        return ans[0]