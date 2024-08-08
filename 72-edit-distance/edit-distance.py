class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1=" "+word1
        word2=" "+word2
        n=len(word1)
        m=len(word2)
        dp=[[0]*(m) for _ in range(n)]
        for r in range(n):
            dp[r][0]=r

        for c in range(m):
            dp[0][c]=c
        # print(dp)
        for r in range(1,n):
            for c in range(1,m):
                if word1[r]==word2[c]:
                    dp[r][c]=dp[r-1][c-1]
                    continue
                replace=dp[r-1][c-1]
                add=dp[r-1][c]
                remove=dp[r][c-1]
                dp[r][c]=min(replace,add,remove)+1
        return dp[n-1][m-1]

