class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Use the shorter dimension for the DP array.
        if n <= m:
            len1 = n
            len2 = m
        else:
            len1 = m
            len2 = n

        dp = [grid[0][0]] * len1
        # Initialize the first row or column, where each cell has one predecessor.
        for k in range(1,len1):
            if n <= m:
                dp[k] = dp[k-1] + grid[0][k]
            else:
                dp[k] = dp[k-1] + grid[k][0]
        for l in range(1,len2):
            if n <= m:
                dp[0] = dp[0] + grid[l][0]
            else:
                dp[0] = dp[0] + grid[0][l]
            for k in range(1,len1):
                # The old dp[k] and updated dp[k-1] represent the two predecessors.
                dp[k] = min(dp[k],dp[k-1])
                if n <= m:
                    dp[k] = dp[k] + grid[l][k]
                else:
                    dp[k] = dp[k] + grid[k][l]
        
        return dp[-1]