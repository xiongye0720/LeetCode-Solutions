class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def DFS(currChar,ans,lvl):
            if lvl == maxLvl:
                ans.append(currChar)
                return
            
            for item in mapping[digits[lvl+1]]:
                DFS(currChar+item,ans,lvl+1)



        mapping = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        maxLvl = len(digits) - 1
        ans = []
        for item in mapping[digits[0]]:
            DFS(item,ans,0)

        return ans
                