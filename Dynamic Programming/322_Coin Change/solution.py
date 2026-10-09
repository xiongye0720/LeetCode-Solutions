class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [(0,0)] * (amount+1)

        for item in coins:
            for i in range(item,amount+1):
                plan2P = dp[i-item][0] + item
                plan2Q = dp[i-item][1] + 1
                if (plan2P>dp[i][0]) or (plan2P==dp[i][0] and plan2Q<dp[i][1]):
                    dp[i] = (plan2P,plan2Q)

        if dp[-1][0] == amount:
            return dp[-1][1]
        else:
            return -1
                
        