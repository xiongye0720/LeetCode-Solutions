class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k <= len(prices):
            dp = [(0,float('-inf'))] * (k+1)
            for i in range(2,len(prices)+1):
                dpPart1 = max(dp[1][0]+prices[i-1]-prices[i-2],prices[i-1]-prices[i-1])
                dp[1] = (dpPart1,max(dp[1]))
                for j in range(2,k+1):
                    dpPart1 = max(dp[j][0]+prices[i-1]-prices[i-2],max(dp[j-1])+prices[i-1]-prices[i-1])
                    dp[j] = (dpPart1,max(dp[j]))
            return max(dp[-1])
        else:
            dp = [(0,float('-inf'))] * (len(prices)+1)
            for j in range(2,len(prices)+1):
                dpPart1 = max(dp[j-1][0]+prices[j-1]-prices[j-2],prices[j-1]-prices[j-1]) 
                dp[j] = (dpPart1,max(dp[j-1]))
            for i in range(2,k+1):
                for j in range(2,len(prices)+1):
                    dpPart1 = max(dp[j-1][0]+prices[j-1]-prices[j-2],max(dp[j])+prices[j-1]-prices[j-1])
                    dp[j] = (dpPart1,max(dp[j-1]))
            return max(dp[-1])