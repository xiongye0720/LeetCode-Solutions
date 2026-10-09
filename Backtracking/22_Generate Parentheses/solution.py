class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def DFS(numOfPar,lPar,proc,ans,tar):
            numOfPar[tar] = numOfPar[tar] - 1
            if tar == 0:
                lPar[0] = lPar[0] + 1
                proc.append('(')
            else:
                lPar[0] = lPar[0] - 1
                proc.append(')')
            
            if numOfPar[0]==0 and numOfPar[1]==0:
                ans.append(''.join(proc))
                numOfPar[tar] = numOfPar[tar] + 1
                proc.pop()
                if tar == 0:
                    lPar[0] = lPar[0] - 1
                else:
                    lPar[0] = lPar[0] + 1
                return

            if lPar[0] > 0:
                if numOfPar[0] == 0:
                    DFS(numOfPar,lPar,proc,ans,1)
                else:
                    DFS(numOfPar,lPar,proc,ans,0)
                    DFS(numOfPar,lPar,proc,ans,1)
            else:
                DFS(numOfPar,lPar,proc,ans,0)

            numOfPar[tar] = numOfPar[tar] + 1
            proc.pop()
            if tar == 0:
                lPar[0] = lPar[0] - 1
            else:
                lPar[0] = lPar[0] + 1


        numOfPar = [n,n]
        lPar = [0]
        proc = []
        ans = []
        DFS(numOfPar,lPar,proc,ans,0)

        return ans


        