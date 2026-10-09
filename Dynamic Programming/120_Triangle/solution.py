class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp[j] stores the minimum path sum to position j in the previous row.
        dp = [triangle[0][0]]
        minVal = dp[0]

        for i in range(1,len(triangle)):
            minVal = float('inf')
            # The left edge has no upper-left parent.
            temMin = float('inf')
            for j in range(i):
                # Save the old value for the next position's upper-left parent.
                temmin = dp[j]
                dp[j] = min(dp[j],temMin) + triangle[i][j]
                temMin = temmin
                minVal = min(dp[j],minVal)
            # The right edge has only an upper-left parent.
            dp.append(temMin+triangle[i][-1])
            minVal = min(dp[-1],minVal)

        return minVal

        