# 279. Perfect Squares

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            tmp = float('inf')
            j = 1
            while j * j <= i:
                tmp = min(min_val, dp[i - j * j] + 1)
                j += 1
            dp[i] = tmp
        return dp[n]
