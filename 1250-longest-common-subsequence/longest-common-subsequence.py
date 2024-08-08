class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for r in range(n-1,-1,-1):
            for c in range(m-1,-1,-1):
                if text1[r]==text2[c]:
                    dp[r][c]=dp[r+1][c+1]+1
                else:
                    dp[r][c]=max(dp[r+1][c],dp[r][c+1])
        return dp[0][0]