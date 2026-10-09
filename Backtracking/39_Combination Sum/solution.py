class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def DFS(proc,rem,lvl,amt,ans):
            proc.append(amt)
            rem[0] = rem[0] - amt*candidates[lvl-1]

            if lvl==maxLvl or rem[0]<candidates[lvl]:
                if rem[0] == 0:
                    temAns = []
                    for i in range(len(proc)):
                        for j in range(proc[i]):
                            temAns.append(candidates[i])
                    ans.append(temAns)
                proc.pop()
                rem[0] = rem[0] + amt*candidates[lvl-1]
                return
            
            for i in range((rem[0]//candidates[lvl])+1):
                DFS(proc,rem,lvl+1,i,ans)
            
            proc.pop()
            rem[0] = rem[0] + amt*candidates[lvl-1]
    
        candidates.sort()
        maxLvl = len(candidates)
        rem = [target]
        ans = []
        proc = []
        if target >= candidates[0]:
            for i in range((target//candidates[0])+1):
                DFS(proc,rem,1,i,ans)
        
        return ans

        