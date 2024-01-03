class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Find LCS Length
        n=len(s)
        dp=[[0]*(n+1) for _ in range(n+1)]

        s2=s[::-1]
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s[i]==s2[j]:
                    dp[i][j]=dp[i+1][j+1]+1
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return n-dp[0][0]

        