class TreeNode:
    def __init__(self):
        self.val = None
        self.endTag = False
        self.child = {}

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def BuildTree(treeNode,tarWord,lvl,maxLvl):
            if lvl == maxLvl:
                treeNode.endTag = True
                return
            if tarWord[lvl] not in treeNode.child:
                temNode = TreeNode()
                temNode.val = tarWord[lvl]
                treeNode.child[tarWord[lvl]] = temNode
            BuildTree(treeNode.child[tarWord[lvl]],tarWord,lvl+1,maxLvl)
        

        def Check(ptr,ans,tNode,dp,s):
            if tNode.endTag and dp[ptr]:
                ans[0] = True
                return
            
            if ptr==0 or (s[ptr-1] not in tNode.child):
                return
            Check(ptr-1,ans,tNode.child[s[ptr-1]],dp,s)


        treeRoot = TreeNode()
        for item in wordDict:
            maxLvl = len(item)
            BuildTree(treeRoot,item[::-1],0,maxLvl)
        
        dp = [True] * (len(s)+1)
        for i in range(1,len(s)+1):
            ans = [False]
            Check(i,ans,treeRoot,dp,s)
            if not ans[0]:
                dp[i] = False
        
        return dp[-1]








        