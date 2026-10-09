class Solution:
    def totalNQueens(self, n: int) -> int:
        def DFS(lvl,pos,vert,pd,nd,ans):
            vert.add(pos)
            pd.add(maxLvl-lvl+pos)
            nd.add(lvl+pos-1)

            if lvl == maxLvl:
                ans[0] = ans[0] + 1
                vert.remove(pos)
                pd.remove(maxLvl-lvl+pos)
                nd.remove(lvl+pos-1)
                return
            for j in range(1,maxLvl+1):
                if (j not in vert) and ((maxLvl-lvl-1+j) not in pd) and ((lvl+j) not in nd):
                    DFS(lvl+1,j,vert,pd,nd,ans)
            
            vert.remove(pos)
            pd.remove(maxLvl-lvl+pos)
            nd.remove(lvl+pos-1)


        maxLvl = n
        ans = [0]
        vert = set()
        pd = set()
        nd = set()
        for j in range(1,maxLvl+1):
            DFS(1,j,vert,pd,nd,ans)

        return ans[0]