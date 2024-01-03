class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1=" "+word1
        word2=" "+word2
        n=len(word1)
        m=len(word2)

        dp=[[0]*(m) for _ in range(n)]

        for r in range(n):
            dp[r][0]=r
        for c in range(m):
            dp[0][c]=c
        

        for i in range(1,n):
            for j in range(1,m):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    insert=dp[i][j-1]+1
                    dele=dp[i-1][j]+1
                    replace=dp[i-1][j-1]+1
                    dp[i][j]=min(insert,dele,replace)
        
        return dp[n-1][m-1]
        