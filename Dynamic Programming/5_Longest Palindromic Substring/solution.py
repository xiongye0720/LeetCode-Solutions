class Solution:
    def longestPalindrome(self, s: str) -> str:
        def CalRadius(lCenter,rCenter,initR,maxId,s):
            while lCenter-initR>=0 and rCenter+initR<=maxId:
                if s[lCenter-initR] != s[rCenter+initR]:
                    return initR
                initR = initR + 1
            return initR


        lCenter = 0
        rCenter = 0
        radius = 1
        rBound = 0
        maxStr = (0,0)
        length = len(s)
        dp = [(1,0)] * length

        for i in range(1,length):
            if i > rBound:
                dp[i] = (CalRadius(i,i,1,length-1,s),CalRadius(i-1,i,0,length-1,s))
            else:
                if lCenter == rCenter:
                    symPt = rCenter - (i - rCenter)
                else:
                    symPt = lCenter - (i - rCenter)
                initR1 = min(dp[symPt][0],rBound-i+1)
                initR2 = min(dp[symPt+1][1],rBound-i+1)
                dp[i] = (CalRadius(i,i,initR1,length-1,s),CalRadius(i-1,i,initR2,length-1,s))
            
            if i+dp[i][0]-1 >= i-1+dp[i][1]:
                if i+dp[i][0]-1 > rBound:
                    rBound = i + dp[i][0] - 1
                    lCenter = i
                    rCenter = i
                    radius = dp[i][0]
            else:
                if i-1+dp[i][1] > rBound:
                    rBound = i - 1 + dp[i][1]
                    lCenter = i - 1
                    rCenter = i
                    radius = dp[i][1]
            if 2*dp[i][0]-1 > 2*dp[i][1]:
                if maxStr[1]-maxStr[0]+1 < 2*dp[i][0]-1:
                    maxStr = (i-(dp[i][0]-1),i+(dp[i][0]-1))
            else:
                if maxStr[1]-maxStr[0]+1 < 2*dp[i][1]:
                    maxStr = (i-dp[i][1],i+dp[i][1]-1)
        
        return s[maxStr[0]:maxStr[1]+1]
 