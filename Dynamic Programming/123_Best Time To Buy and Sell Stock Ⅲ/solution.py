class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        dp = [(0,float('-inf'))] * 2
        for j in range(2,len(prices)+1):
            dpPart1 = max(dp[0][0]+prices[j-1]-prices[j-2],prices[j-1]-prices[j-1])
            dp[0] = (dpPart1,max(dp[0]))
            dpPart1 = max(dp[1][0]+prices[j-1]-prices[j-2],max(dp[0])+prices[j-1]-prices[j-1])
            dp[1] = (dpPart1,max(dp[1]))
        
        return max(dp[1])
        