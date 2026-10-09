class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        if m <= n:
            if matrix[0][0] == '1':
                dp = [1] * m
            else:
                dp = [0] * m
            maxLen = dp[0]
            for i in range(1,m):
                if matrix[i][0] == '1':
                    dp[i] = 1
                else:
                    dp[i] = 0
                maxLen = max(maxLen,dp[i])
            
            for j in range(1,n):
                if matrix[0][j] == '1':
                    dp[0] = 1
                else:
                    dp[0] = 0
                maxLen = max(maxLen,dp[0])
                for i in range(1,m):
                    if matrix[i][j] == '0':
                        dp[i] = 0
                    else:
                        if dp[i]==0 or dp[i-1]==0:
                            dp[i] = 1
                        else:
                            if dp[i] == dp[i-1]:
                                if matrix[i-dp[i]][j-dp[i]] == '1':
                                    dp[i] = dp[i] + 1
                            else:
                                dp[i] = min(dp[i],dp[i-1]) + 1
                    maxLen = max(maxLen,dp[i])
        else:
            if matrix[0][0] == '1':
                dp = [1] * n
            else:
                dp = [0] * n
            maxLen = dp[0]
            for j in range(1,n):
                if matrix[0][j] == '1':
                    dp[j] = 1
                else:
                    dp[j] = 0
                maxLen = max(maxLen,dp[j])
        
            for i in range(1,m):
                if matrix[i][0] == '1':
                    dp[0] = 1
                else:
                    dp[0] = 0
                maxLen = max(maxLen,dp[0])
                for j in range(1,n):
                    if matrix[i][j] == '0':
                        dp[j] = 0
                    else:
                        if dp[j-1]==0 or dp[j]==0:
                            dp[j] = 1
                        else:
                            if dp[j-1] == dp[j]:
                                if matrix[i-dp[j]][j-dp[j]] == '1':
                                    dp[j] = dp[j] + 1
                            else:
                                dp[j] = min(dp[j-1],dp[j]) + 1
                    maxLen = max(maxLen,dp[j])
        
        return maxLen * maxLen