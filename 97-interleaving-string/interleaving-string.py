class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2) !=len(s3):
            return False

        n=len(s1)
        m=len(s2)
        p=len(s3)

        dp=[[False]*(m+1) for _ in range(n+1)]

        for i in range(n,-1,-1):
            for j in range(m,-1,-1):
                if i==n and j==m:
                    dp[i][j]=True
                    continue
                if i<n and s1[i]==s3[i+j] and dp[i+1][j]:
                    dp[i][j]=True
                if j<m and s2[j]==s3[i+j] and dp[i][j+1]:
                    dp[i][j]=True
        return dp[0][0]
        
        # if len(s1)+len(s2) !=len(s3):
        #     return False

        # dp={}

        # def isInterleaving(i,j):
        #     if i==len(s1) and j==len(s2):
        #         return True
            
        #     if (i,j) in dp:
        #         return dp[(i,j)]

        #     if i<len(s1) and s1[i]==s3[i+j] and isInterleaving(i+1,j):
        #         dp[(i,j)]=True
        #         return True
        #     if j<len(s2) and s2[j]==s3[i+j] and isInterleaving(i,j+1):
        #         dp[(i,j)]=True
        #         return True
            
        #     dp[(i,j)]=False
        #     return False

        # return isInterleaving(0,0)
        