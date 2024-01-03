class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        lcs=self.findLCS(str1,str2)
        i,j=0,0
        res=""
        for c in lcs:
            # Add char upto c 
            while str1[i]!=c:
                res+=str1[i]
                i+=1
            while str2[j]!=c:
                res+=str2[j]
                j+=1
            
            # add c 
            res+=c
            # Since both i and j are at c
            i+=1
            j+=1
        # Add remaining chars
        res+=str1[i:]+str2[j:]
        return res

            



    def findLCS(self,s1,s2):

        n=len(s1)
        m=len(s2)

        dp=[[0]*(m+1) for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if s1[i]==s2[j]:
                    dp[i][j]=dp[i+1][j+1]+1
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        
        lcs=""
        i,j=0,0
        while i<n and j<m: 
            if s1[i]==s2[j]:
                lcs+=s1[i]
                i+=1
                j+=1
            elif dp[i+1][j]> dp[i][j+1]:
                i+=1
            else:
                j+=1
        
        return lcs